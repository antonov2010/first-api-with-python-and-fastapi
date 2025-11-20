"""
models/item.py
Modelo Pydantic para Artículo de inventario.

Este archivo define la estructura de los datos que representan un artículo en el inventario.
Utiliza Pydantic para validar automáticamente los datos recibidos en la API.
"""
from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    """
    Modelo de datos para un artículo de inventario.
    Cada campo tiene validaciones y descripciones para facilitar el uso y la documentación automática.
    """
    id: int = Field(..., description="Identificador único del artículo")
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre del artículo")
    descripcion: Optional[str] = Field(None, max_length=250, description="Descripción del artículo")
    cantidad: int = Field(..., ge=0, description="Cantidad disponible en inventario")

    class Config:
        # Ejemplo de datos para la documentación interactiva
        schema_extra = {
            "example": {
                "id": 1,
                "nombre": "Laptop",
                "descripcion": "Computadora portátil de 15 pulgadas",
                "cantidad": 10
            }
        }
