
📝 API de Inventario Simple y Segura

Repositorio: https://github.com/antonov2010/first-api-with-python-and-fastapi

Descripción
-----------
Proyecto de ejemplo para un taller: una API REST construida con FastAPI que gestiona un inventario simple de "Artículos". Está pensada para ser didáctica, incluyendo validación con Pydantic, documentación automática (Swagger) y un mecanismo básico de autenticación/autorizarción para proteger endpoints sensibles.

Características principales
-------------------------
- CRUD de `Item` (crear, listar, obtener por id, actualizar, eliminar).
- Autenticación mediante formulario (OAuth2 Password Flow) y token de acceso (simulado).
- Base de datos en memoria (`app/core/database.py`) — ideal para demos y talleres.
- Documentación interactiva disponible vía Swagger UI.

Requisitos
---------
- Python 3.13.9
- Recomendado: crear y activar un entorno virtual antes de instalar dependencias.

Instalación rápida
------------------
1. Crear y activar el entorno virtual ( Bash / Linux ):

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # opcional: herramientas de desarrollo
```

3. Ejecutar la API en modo desarrollo:

```bash
uvicorn main:app --reload
```

La API quedará accesible en `http://localhost:8000` y la documentación Swagger en `http://localhost:8000/docs`.

Endpoints principales
---------------------
- `GET /` — health check, retorna un mensaje simple.
- `GET /items/` — lista todos los artículos.
- `POST /items/` — crea un artículo (protegido: solo admin).
- `GET /items/{item_id}` — obtiene detalles de un artículo.
- `PUT /items/{item_id}` — actualiza un artículo.
- `DELETE /items/{item_id}` — elimina un artículo.
- `POST /auth/token` — endpoint de login (OAuth2 Password Flow). Devuelve `access_token`.

Autenticación y pruebas
-----------------------
Este proyecto usa un token simulado para simplificar la explicación del flujo OAuth2.

- Usuarios de prueba (almacenados en `app/core/users.py`):
	- admin / admin123  (rol: `admin`)
	- viewer / viewer123 (rol: `viewer`)

- Para obtener un token (ejemplo con `curl`):

```bash
curl -X POST -F 'username=admin' -F 'password=admin123' http://localhost:8000/auth/token
# Respuesta: {"access_token":"fake-token-for-admin","token_type":"bearer","role":"admin"}
```

- Usar el token para llamar a un endpoint protegido (`POST /items/`):

```bash
curl -X POST http://localhost:8000/items/ \
	-H "Authorization: Bearer fake-token-for-admin" \
	-H "Content-Type: application/json" \
	-d '{"id":10,"nombre":"Monitor","descripcion":"24 pulgadas","cantidad":5}'
```

Notas sobre Swagger UI
---------------------
- En `/docs` puedes usar el endpoint `POST /auth/token` con el formulario que Swagger provee (OAuth2PasswordRequestForm). Swagger enviará los datos como `x-www-form-urlencoded` y devolverá el token.
- Para probar endpoints protegidos desde Swagger, usa el botón "Authorize" e introduce el token: `Bearer <access_token>`.

Limitaciones y recomendaciones
------------------------------
- Seguridad: este repositorio emplea contraseñas en texto plano y tokens simulados — aceptable para un taller, NO para producción.
- Para producción recomienda:
	- Usar JWT firmado y validado (p. ej. `python-jose`).
	- Hashear contraseñas con `bcrypt`/`passlib`.
	- Implementar expiración de tokens y refresh tokens.

Archivos importantes
-------------------
- `main.py` — punto de entrada y registro de routers.
- `app/models/item.py` — modelo Pydantic `Item`.
- `app/routes/items.py` — rutas CRUD para artículos.
- `app/routes/auth.py` — endpoint de autenticación.
- `app/core/database.py` — base de datos simulada en memoria.
- `app/core/users.py` — usuarios de prueba y autenticación básica.
- `app/core/security.py` — dependencia `get_current_user` que extrae el usuario desde el token.
- `avance.md` — seguimiento de historias y avance del proyecto.

Soporte y contribuciones
-------------------------
Si vas a usar este proyecto para un taller, puedes:
- Modificar `USERS_DB` para agregar más usuarios de prueba.
- Extender la simulación de base de datos o conectar una DB real (SQLite, Postgres).

Si quieres que implemente JWT real y hashing de contraseñas para un ejemplo más seguro, dime y lo añado.

Documentación interactiva
-------------------------
Swagger UI: `http://localhost:8000/docs`

¡Listo! Usa los endpoints y dime si quieres que mejore la seguridad, agregue pruebas unitarias o prepare una guía de taller más extensa.