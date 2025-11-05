# supervisor_ui/models.py
import json
from werkzeug.security import check_password_hash

class User:
    def __init__(self, email, name, role):
        self.id = email
        self.email = email
        self.name = name
        self.role = role

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

def load_user_by_email(email):
    try:
        with open("supervisors.json", "r") as f:
            data = json.load(f)
        user = data.get(email)
        if not user:
            return None
        return User(email=user["email"], name=user.get("name", ""), role=user.get("role", "supervisor"))
    except FileNotFoundError:
        return None

def verify_password(email, password):
    try:
        with open("supervisors.json", "r") as f:
            data = json.load(f)
        user = data.get(email)
        if not user:
            return False
        return check_password_hash(user["password"], password)
    except FileNotFoundError:
        return False
