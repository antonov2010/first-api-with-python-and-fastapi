API de Inventario — Documentación técnica
-----------
Proyecto de ejemplo para talleres: una API REST construida con FastAPI que gestiona un inventario simple de "artículos". Es didáctica y muestra buenas prácticas básicas con Pydantic, documentación automática (Swagger) y un mecanismo simple de autenticación/autorizarción para proteger endpoints sensibles.

Características principales
--------------------------
- CRUD de `Item`: crear, listar, obtener por id, actualizar y eliminar.
- Autenticación mediante formulario (OAuth2 Password Flow) con token simulado.
- Base de datos en memoria (`app/core/database.py`) — ideal para demos y pruebas.
- Documentación interactiva vía Swagger UI (`/docs`).

Requisitos
---------
- Python 3.10+ (el proyecto indica 3.13.9, usar la versión disponible estable).
- Recomendada: crear y activar un entorno virtual antes de instalar dependencias.
# API de Inventario — Documentación técnica

Repositorio: https://github.com/antonov2010/first-api-with-python-and-fastapi

## Descripción

Este repositorio contiene una API REST desarrollada con FastAPI destinada a gestionar un inventario simple de artículos. El proyecto tiene un propósito didáctico y se emplea para demostraciones y talleres, mostrando validación con Pydantic, documentación automática (OpenAPI/Swagger) y un mecanismo básico de autenticación para proteger determinados endpoints.
# API de Inventario — Documentación técnica

Repositorio: https://github.com/antonov2010/first-api-with-python-and-fastapi

## Descripción

Este repositorio contiene una API REST desarrollada con FastAPI destinada a gestionar un inventario simple de artículos. El proyecto tiene un propósito didáctico y se emplea para demostraciones y talleres, mostrando validación con Pydantic, documentación automática (OpenAPI/Swagger) y un mecanismo básico de autenticación para proteger determinados endpoints.

## Alcance

- Implementación de operaciones CRUD sobre el recurso `Item`.
- Mecanismo de autenticación mediante OAuth2 Password Flow (token simulado para ejemplos).
- Almacenamiento en memoria (simulación) a fin de facilitar pruebas y enseñanza.

## Requisitos

- Python 3.10 o superior. Si se dispone de la versión indicada en el repositorio (3.13.9), podrá utilizarse igualmente.
- Recomendación: crear y utilizar un entorno virtual para instalar dependencias y ejecutar la aplicación.

## Instalación y ejecución

1) Crear y activar un entorno virtual.

Windows (PowerShell):

```powershell
python -m venv .venv
```

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux / macOS (bash/zsh):

```bash
python -m venv .venv
```

```bash
source .venv/bin/activate
```

2) Instalar dependencias:

```bash
pip install -r requirements.txt
```

```bash
# (Opcional) herramientas de desarrollo
pip install -r requirements-dev.txt
```

3) Iniciar la aplicación en modo desarrollo:

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://localhost:8000`. La documentación interactiva (Swagger UI) estará en `http://localhost:8000/docs`.

### Comandos útiles de desarrollo

- Formatear el código con `black`:

```bash
black .
```

- Verificar estilo con `flake8`:

```bash
flake8
```

- Nota sobre pruebas: actualmente no hay tests incluidos en el repositorio. Para añadir pruebas se recomienda usar `pytest`; una vez añadidos los tests, ejecutar:

```bash
pytest
```

## Endpoints principales

- `GET /` — Verificación de estado (health check).
- `GET /items/` — Listado de artículos.
- `POST /items/` — Creación de un artículo (protegido; requiere rol `admin`).
- `GET /items/{item_id}` — Obtención de un artículo por identificador.
- `PUT /items/{item_id}` — Actualización de un artículo.
- `DELETE /items/{item_id}` — Eliminación de un artículo.
-- `POST /auth/token` — Autenticación mediante OAuth2 Password Flow; devuelve `access_token` (token simulado para el ejemplo).

## Autenticación y pruebas

Para facilitar demostraciones, el sistema emplea tokens simulados y usuarios de prueba definidos en `app/core/users.py`.

Usuarios de prueba:

- `admin` / `admin123` (rol: `admin`)
- `viewer` / `viewer123` (rol: `viewer`)

### Ejemplo: obtención de token mediante `curl`

```bash
curl -X POST -F 'username=admin' -F 'password=admin123' http://localhost:8000/auth/token
# Ejemplo de respuesta: {"access_token":"fake-token-for-admin","token_type":"bearer","role":"admin"}
```

### Ejemplo: llamada a endpoint protegido (`POST /items/`) usando el token

```bash
curl -X POST http://localhost:8000/items/ \
	-H "Authorization: Bearer fake-token-for-admin" \
	-H "Content-Type: application/json" \
	-d '{"id":10,"nombre":"Monitor","descripcion":"24 pulgadas","cantidad":5}'
```

## Documentación (Swagger UI)

La documentación generada por OpenAPI está disponible en `/docs`. Desde esa interfaz se puede utilizar el formulario de `POST /auth/token` (envío `x-www-form-urlencoded`) y autorizar solicitudes mediante el botón "Authorize" con el esquema `Bearer <access_token>`.

## Consideraciones de seguridad (producción)

Este proyecto emplea contraseñas en texto plano y tokens simulados con fines didácticos; no está preparado para su uso en producción. Para un despliegue seguro se recomienda al menos:

- Utilizar JWT firmados y verificados (por ejemplo, `python-jose`).
- Almacenar contraseñas con hashing seguro (por ejemplo, `passlib` con `bcrypt`).
- Implementar caducidad de tokens y mecanismo de refresh.
- Forzar HTTPS en el entorno de producción y validar orígenes según sea necesario.

## Detalles técnicos y comportamiento de los endpoints

- Modelo `Item` (definido en `app/models/item.py`):
	- `id` (int): Identificador único del artículo.
	- `nombre` (str): Nombre del artículo (1–100 caracteres).
	- `descripcion` (str, opcional): Descripción del artículo (máx. 250 caracteres).
	- `cantidad` (int): Cantidad disponible (>= 0).

- Comportamiento de las rutas principales (`app/routes/items.py`):
	- `GET /items/` — Devuelve la lista completa de artículos. No requiere autenticación.
	- `POST /items/` — Crea un artículo; exige autenticación y rol `admin`. Retorna `201 Created` con el recurso creado.
	- `GET /items/{item_id}` — Recupera un artículo por su `id`; retorna `404` si no existe.
	- `PUT /items/{item_id}` — Reemplaza/actualiza un artículo por su `id`; retorna `404` si no existe.
	- `DELETE /items/{item_id}` — Elimina un artículo por su `id`; retorna `204 No Content` si la eliminación fue exitosa.

## Ejecución en entornos distintos a desarrollo

En entornos de staging o producción se recomienda ejecutar `uvicorn` con opciones de rendimiento y detrás de un servidor/proxy (por ejemplo, `gunicorn` con workers y `uvicorn.workers.UvicornWorker`). Ejemplo básico con `gunicorn`:

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

## Estructura del repositorio y archivos relevantes

- `main.py` — Punto de entrada y registro de routers.
- `app/models/item.py` — Definición del modelo Pydantic `Item`.
- `app/routes/items.py` — Implementación de las rutas CRUD para artículos.
- `app/routes/auth.py` — Endpoint de autenticación y emisión de token (simulado).
- `app/core/database.py` — Implementación de la base de datos en memoria.
- `app/core/users.py` — Usuarios de prueba y lógica de autenticación básica.
- `app/core/security.py` — Dependencia `get_current_user` y verificación del token.
- `avance.md` — Registro de avance y tareas relacionadas con el proyecto.

## Soporte y contribuciones

Las contribuciones pueden realizarse mediante pull requests o abriendo issues en el repositorio. Para usos de taller se recomienda modificar `USERS_DB` para ajustar los usuarios de prueba o reemplazar la capa de persistencia por una base de datos real (SQLite, Postgres, etc.).

## Solución de problemas conocidos (Windows)

- En PowerShell, la política de ejecución de scripts puede impedir la activación del entorno virtual. Para permitirla:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

- Actualizar la herramienta `pip`:

```powershell
python -m pip install --upgrade pip
```

- Comprobar las versiones de Python y pip:

```powershell
python --version
pip --version
```

## Autor y contacto

**Autor:** Neri Ramirez

**Rol:** Autor principal / Mantenedor

**GitHub:** https://github.com/antonov2010

**Email:** neri.ramirez549@gmail.com


## Licencia

Consulte el fichero `LICENSE` incluido en el repositorio para información sobre la licencia del proyecto.

## Contacto adicional

Para consultas técnicas y reportes de errores, se recomienda utilizar el sistema de issues del repositorio.

