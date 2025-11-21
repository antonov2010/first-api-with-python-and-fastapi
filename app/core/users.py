"""
core/users.py
Simulación de usuarios y autenticación en memoria.

Este archivo define los usuarios de prueba y la función para validar credenciales.
No se utiliza una base de datos real de usuarios, solo un diccionario en memoria.
"""
from typing import Dict, Optional
from pydantic import BaseModel

class User(BaseModel):
    """
    Modelo de datos para usuario del sistema.
    Incluye nombre de usuario, contraseña y rol (admin o viewer).
    """
    username: str
    password: str
    role: str

USERS_DB: Dict[str, User] = {
    # Usuarios de ejemplo para autenticación
    "admin": User(username="admin", password="admin123", role="admin"),
    "viewer": User(username="viewer", password="viewer123", role="viewer")
}

def authenticate_user(username: str, password: str) -> Optional[User]:
    """
    Verifica si el usuario y la contraseña son correctos.
    Retorna el usuario si las credenciales coinciden, None si no.
    """
    user = USERS_DB.get(username)
    if user and user.password == password:
        return user
    return None
