import os
import firebase_admin
from firebase_admin import credentials, firestore

# Automatically build the correct path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # goes up from /db to project root
cred_path = os.path.join(BASE_DIR, "config", "firebase_key.json")

# Initialize Firebase
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

print("✅ Firebase connection successful!")
