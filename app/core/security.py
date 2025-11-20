"""
core/security.py
Dependencia de seguridad para obtener el usuario actual desde el token enviado en la solicitud.

Este módulo provee una dependencia `get_current_user` que puede usarse con `Depends()` en
endpoints para forzar autenticación. En este proyecto didáctico se utiliza un token "falso"
con el prefijo `fake-token-for-<username>`. La función valida la forma del token y busca
el usuario correspondiente en `USERS_DB`.

Notas:
- En un proyecto real se reemplazaría la lógica de decodificación por la verificación de
  un JWT mediante bibliotecas como `python-jose` o `PyJWT`.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.users import USERS_DB, User

# OAuth2PasswordBearer configura la dependencia que extrae el token Bearer de la
# cabecera `Authorization: Bearer <token>`. `tokenUrl` es la ruta donde el cliente
# obtiene el token (nuestro endpoint de login: /auth/token).
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """
    Dependencia que devuelve el `User` asociado al token proporcionado.

    Comportamiento (simplificado):
    - Verifica que el token comience con el prefijo `fake-token-for-`.
    - Extrae el nombre de usuario del token y busca el usuario en `USERS_DB`.
    - Si el token es inválido o el usuario no existe, lanza `HTTPException(401)`.

    Uso:
        current_user: User = Depends(get_current_user)

    Retorna:
        User -- objeto Pydantic con los datos del usuario autenticado.
    """
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
