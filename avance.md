# Plan de trabajo y avance de historias de usuario

| Historia         | Descripción breve                                      | Estado      |
|-----------------|--------------------------------------------------------|-------------|
| historia-1.1.md | Estructura base FastAPI y documentación automática     | Completada  |
| historia-1.2.md | Modelo de artículo y rutas CRUD                       | Completada  |
| historia-1.3.md | Simulación de base de datos en memoria                | Completada  |

---

## Detalle de avance
- Se creó la estructura base del proyecto siguiendo buenas prácticas.
- Se implementó el archivo main.py con la instancia de FastAPI y el endpoint raíz.
- La documentación Swagger está disponible en /docs.

- Se creó el modelo Pydantic para artículo (id, nombre, descripción, cantidad).
- Se implementaron y registraron las rutas CRUD para artículos en la API.
- Los endpoints CRUD pueden probarse desde /docs.

---

- Se creó el archivo app/core/database.py con una lista global DATABASE.
- La lista DATABASE se inicializa con 3 artículos de prueba.
- Las rutas CRUD ahora utilizan la base de datos simulada.

Actualiza este documento conforme avancemos en nuevas historias.
