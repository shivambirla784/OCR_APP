# OCR_APP
An OCR (Optical Character Recognition) App that can recognize thai id cards and get the required information
This README provides instructions for setting up and running the Optical Character Recognition (OCR) App. The application is designed to recognize Thai ID cards, extract relevant information using Google Vision API, and store the data in a MongoDB database. The tech stack includes Python (Flask), React, Node.js, and MongoDB.

Table of Contents
1.Setup Instructions

2.Dependencies

3.Overview of Architecture

1. Setup Instructions
Backend (Flask - Python)
Install Python (https://www.python.org/downloads/).

Install required Python packages:

Copy code
pip install flask flask-cors pymongo google-cloud-vision
Set up Google Cloud Vision API:

Create a Google Cloud Platform (GCP) project and enable the Vision API.
Download the API credentials JSON file and set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of the JSON file.
Install MongoDB (https://www.mongodb.com/try/download/community).

Start the MongoDB server.

Run the Flask backend:

Copy code
python app.py
Frontend (React)
Install Node.js (https://nodejs.org/).
Navigate to the frontend directory:
bash
Copy code
cd frontend
Install dependencies:
Copy code
npm install
Run the React app:
sql
Copy code
npm start
2. Dependencies
Backend (Flask - Python)
Flask
Flask-CORS
pymongo
google-cloud-vision
Frontend (React)
React
Axios
3. Overview of Architecture
The application follows a client-server architecture:

Backend (Flask):

Provides RESTful APIs for OCR processing and CRUD operations.
Uses Google Vision API for OCR processing.
Stores OCR results in a MongoDB database.
Frontend (React):

Allows users to upload Thai ID card images.
Sends image data to the Flask backend for OCR processing.
