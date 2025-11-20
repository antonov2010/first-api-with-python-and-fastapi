"""
routes/items.py
Rutas CRUD para gestión de artículos en inventario.
"""
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.item import Item

router = APIRouter(prefix="/items", tags=["items"])

# Almacenamiento en memoria
items_db: List[Item] = []

@router.get("/", response_model=List[Item])
def list_items():
    """Listar todos los artículos."""
    return items_db

@router.post("/", response_model=Item, status_code=201)
def create_item(item: Item):
    """Crear un nuevo artículo."""
    if any(i.id == item.id for i in items_db):
        raise HTTPException(status_code=400, detail="ID de artículo ya existe.")
    items_db.append(item)
    return item

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    """Obtener un artículo por ID."""
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Artículo no encontrado.")

@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    """Actualizar un artículo existente."""
    for idx, i in enumerate(items_db):
        if i.id == item_id:
            items_db[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Artículo no encontrado.")

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int):
    """Eliminar un artículo por ID."""
    for idx, i in enumerate(items_db):
        if i.id == item_id:
            items_db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Artículo no encontrado.")
