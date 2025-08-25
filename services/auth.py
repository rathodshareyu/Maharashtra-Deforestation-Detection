import hashlib


# Simple in-memory user store (replace with DB in production)
users = {"admin": hashlib.sha256("admin123".encode()).hexdigest()}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def validate_user(username: str, password: str) -> bool:
    return users.get(username) == hash_password(password)

def register_user(username: str, password: str) -> bool:
    if username in users:
        return False
    users[username] = hash_password(password)
    return True

