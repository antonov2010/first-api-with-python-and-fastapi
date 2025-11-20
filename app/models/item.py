"""
models/item.py
Modelo Pydantic para Artículo de inventario.
"""
from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    id: int = Field(..., description="Identificador único del artículo")
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre del artículo")
    descripcion: Optional[str] = Field(None, max_length=250, description="Descripción del artículo")
    cantidad: int = Field(..., ge=0, description="Cantidad disponible en inventario")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "nombre": "Laptop",
                "descripcion": "Computadora portátil de 15 pulgadas",
                "cantidad": 10
            }
        }
