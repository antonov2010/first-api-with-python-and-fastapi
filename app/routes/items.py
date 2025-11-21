"""
routes/items.py
Rutas CRUD para gestión de artículos en inventario.

Este archivo define los endpoints para crear, leer, actualizar y eliminar artículos.
Utiliza una base de datos simulada en memoria y aplica validaciones y autorización.
"""
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.item import Item

from app.core.database import DATABASE
from app.core.security import get_current_user
from app.core.users import User


# Creamos el router para agrupar las rutas relacionadas con artículos
router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=List[Item])
def list_items():
    """
    Devuelve la lista completa de artículos en el inventario.
    No requiere autenticación.
    """
    return DATABASE

@router.post("/", response_model=Item, status_code=201)
def create_item(item: Item, current_user: User = Depends(get_current_user)):
    """
    Crea un nuevo artículo en el inventario.
    Solo el usuario con rol 'admin' puede acceder a este endpoint.
    Valida que el ID no esté repetido.
    """
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para crear artículos.")
    if any(i.id == item.id for i in DATABASE):
        raise HTTPException(status_code=400, detail="ID de artículo ya existe.")
    DATABASE.append(item)
    return item

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    """
    Devuelve los detalles de un artículo específico por su ID.
    Retorna error 404 si no existe.
    """
    for item in DATABASE:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Artículo no encontrado.")

@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    """
    Actualiza los datos de un artículo existente por su ID.
    Retorna error 404 si no existe.
    """
    for idx, i in enumerate(DATABASE):
        if i.id == item_id:
            DATABASE[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Artículo no encontrado.")

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int):
    """
    Elimina un artículo del inventario por su ID.
    Retorna error 404 si no existe.
    """
    for idx, i in enumerate(DATABASE):
        if i.id == item_id:
            DATABASE.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Artículo no encontrado.")
