"""
routes/items.py
Rutas CRUD para gestión de artículos en inventario.
"""
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.item import Item

from app.core.database import DATABASE
from app.core.security import get_current_user
from app.core.users import User

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=List[Item])
def list_items():
    """Listar todos los artículos."""
    return DATABASE

@router.post("/", response_model=Item, status_code=201)
def create_item(item: Item, current_user: User = Depends(get_current_user)):
    """Crear un nuevo artículo (solo admin)."""
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para crear artículos.")
    if any(i.id == item.id for i in DATABASE):
        raise HTTPException(status_code=400, detail="ID de artículo ya existe.")
    DATABASE.append(item)
    return item

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    """Obtener un artículo por ID."""
    for item in DATABASE:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Artículo no encontrado.")

@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    """Actualizar un artículo existente."""
    for idx, i in enumerate(DATABASE):
        if i.id == item_id:
            DATABASE[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Artículo no encontrado.")

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int):
    """Eliminar un artículo por ID."""
    for idx, i in enumerate(DATABASE):
        if i.id == item_id:
            DATABASE.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Artículo no encontrado.")
