import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # services/
DATA_FILE = os.path.join(BASE_DIR, "..", "data", "users.json")

def load_users():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def validate_user(username, password):
    users = load_users()
    # Debugging
    print("DEBUG USERS:", users)
    print("INPUT:", username, password)
    return username in users and users[username] == password
