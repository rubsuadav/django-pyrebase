import pyrebase
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials
from google.cloud.firestore_v1 import Client as FirestoreClient


load_dotenv()

# Firebase configuration

config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": "integracion-django.appspot.com",
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)

# Initialize Firebase Authentication
auth = firebase.auth()

# Initialize Firebase Storage
storage = firebase.storage()

# Initialize Firebase only if it's not already initialized

if not firebase_admin._apps:
    firebase_admin.initialize_app(credentials.Certificate(
        os.environ.get("GOOGLE_APPLICATION_CREDENTIALS2")))

# Initialize Firebase Firestore
firestore = FirestoreClient()
