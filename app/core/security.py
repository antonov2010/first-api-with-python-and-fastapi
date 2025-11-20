"""
core/security.py
Dependencia para obtener el usuario actual a partir del token.
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.users import USERS_DB, User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# Simulación de decodificación de token

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    if not token.startswith("fake-token-for-"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    username = token.replace("fake-token-for-", "")
    user = USERS_DB.get(username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
