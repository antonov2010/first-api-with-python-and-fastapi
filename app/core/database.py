"""
core/database.py
Simulación de base de datos en memoria para artículos.
"""
from app.models.item import Item
from typing import List

DATABASE: List[Item] = [
    Item(id=1, nombre="Laptop", descripcion="Computadora portátil", cantidad=10),
    Item(id=2, nombre="Mouse", descripcion="Ratón inalámbrico", cantidad=25),
    Item(id=3, nombre="Teclado", descripcion="Teclado mecánico", cantidad=15)
]
