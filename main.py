"""
main.py
Configuración base de la aplicación FastAPI.
"""

from fastapi import FastAPI
from app.routes.items import router as items_router

app = FastAPI(title="API de Inventario Simple y Segura")

app.include_router(items_router)

@app.get("/")
def read_root():
    """Endpoint raíz para verificar el estado de la API."""
    return {"message": "API de Inventario activa"}
