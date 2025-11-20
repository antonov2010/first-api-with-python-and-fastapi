"""
core/users.py
Simulación de usuarios y autenticación en memoria.
"""
from typing import Dict, Optional
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    role: str

# Diccionario de usuarios hardcoded
USERS_DB: Dict[str, User] = {
    "admin": User(username="admin", password="admin123", role="admin"),
    "viewer": User(username="viewer", password="viewer123", role="viewer")
}

def authenticate_user(username: str, password: str) -> Optional[User]:
    user = USERS_DB.get(username)
    if user and user.password == password:
        return user
    return None
