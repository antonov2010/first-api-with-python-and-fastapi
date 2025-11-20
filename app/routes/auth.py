"""
routes/auth.py
Endpoint de autenticación y generación de token (placeholder).

Este archivo define el endpoint para que los usuarios puedan iniciar sesión y obtener un token de acceso.
Utiliza un flujo simplificado de OAuth2 y un token simulado para propósitos educativos.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.core.users import authenticate_user, User

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint para autenticación de usuario.
    Recibe usuario y contraseña mediante un formulario y verifica las credenciales.
    Si son correctas, retorna un token de acceso simulado y el rol del usuario.
    En producción, aquí se generaría un JWT real.
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Token placeholder (en producción usar JWT real)
    token = f"fake-token-for-{user.username}"
    return {"access_token": token, "token_type": "bearer", "role": user.role}
