# app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
from google.cloud import vision
from google.cloud.vision import types
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['ocr_database']
collection = db['ocr_data']

# Google Vision API setup
def process_image(image_path):
    client = vision.ImageAnnotatorClient()
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    return response.text_annotations[0].description if response.text_annotations else None

# CRUD API
@app.route('/ocr', methods=['POST'])
def create_ocr_data():
    if 'image_path' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_path = request.files['image_path']
    ocr_result = process_image(image_path)

    if ocr_result:
        data = {'id_card_info': ocr_result.decode('utf-8')}
        result = collection.insert_one(data)
        return jsonify({'message': 'OCR data created successfully', 'id': str(result.inserted_id)})
    else:
        return jsonify({'error': 'OCR processing failed'}), 500

@app.route('/ocr/<id>', methods=['GET'])
def get_ocr_data(id):
    data = collection.find_one({'_id': ObjectId(id)})
    return jsonify({'id_card_info': data['id_card_info']}) if data else jsonify({'error': 'OCR data not found'}), 404

# Add update and delete routes as needed

if __name__ == '__main__':
    app.run(debug=True)
