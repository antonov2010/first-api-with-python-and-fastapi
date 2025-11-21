"""
core/database.py
Simulación de base de datos en memoria para artículos.

Este archivo define una lista global llamada DATABASE que simula una base de datos.
Aquí se almacenan los artículos creados y modificados durante la ejecución de la API.
No se utiliza una base de datos real para facilitar el aprendizaje y la prueba.
"""
from app.models.item import Item
from typing import List

DATABASE: List[Item] = [
    # Artículos de ejemplo para iniciar la API con datos
    Item(id=1, nombre="Laptop", descripcion="Computadora portátil", cantidad=10),
    Item(id=2, nombre="Mouse", descripcion="Ratón inalámbrico", cantidad=25),
    Item(id=3, nombre="Teclado", descripcion="Teclado mecánico", cantidad=15)
]
