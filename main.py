"""
main.py
Configuración base de la aplicación FastAPI.
"""

from fastapi import FastAPI

app = FastAPI(title="API de Inventario Simple y Segura")

# Importar y registrar rutas aquí
# from app.routes import ...

@app.get("/")
def read_root():
    """Endpoint raíz para verificar el estado de la API."""
    return {"message": "API de Inventario activa"}
