
"""
main.py
Archivo principal de la API de Inventario Simple y Segura.

Este archivo es la puerta de entrada de la aplicación. Aquí se configura la instancia principal de FastAPI,
se registran los routers (módulos de rutas) y se define el endpoint raíz para verificar el estado de la API.
"""

from fastapi import FastAPI

# Importamos los routers que contienen las rutas de la API
from app.routes.items import router as items_router  # Rutas CRUD de artículos
from app.routes.auth import router as auth_router    # Rutas de autenticación

# Creamos la instancia principal de FastAPI
app = FastAPI(title="API de Inventario Simple y Segura")

# Registramos los routers en la aplicación principal
app.include_router(items_router)
app.include_router(auth_router)

@app.get("/")
def read_root():
    """
    Endpoint raíz para verificar el estado de la API.
    Retorna un mensaje simple si la API está activa.
    """
    return {"message": "API de Inventario activa"}
