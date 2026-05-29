# Back-End-UCI

Backend desarrollado en Python para la plataforma UCI. Este servicio se encarga de la gestión de datos, autenticación de usuarios, comunicación con la base de datos y exposición de servicios mediante una API REST para el frontend.

## Características

- API REST desarrollada en Python.
- Gestión de usuarios y autenticación.
- Conexión y administración de base de datos.
- Organización modular mediante rutas y servicios.
- Integración con aplicaciones frontend.

## Estructura del proyecto

```text
Back-End-UCI/
├── common/
├── db/
├── routes/
├── app.py
├── db_init.py
├── requirements.txt
└── README.md
```

## Tecnologías utilizadas

- Python
- Flask
- SQLAlchemy
- MySQL
- JWT Authentication

## Requisitos

Tener instalado:

```bash
python --version
pip --version
```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Ana-toba/Back-End-UCI.git
```

Ingresar al directorio del proyecto:

```bash
cd Back-End-UCI
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / MacOS

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Configuración

Crear un archivo `.env` con las variables de entorno necesarias para la conexión a la base de datos y la configuración de la aplicación.

Ejemplo:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=usuario
DB_PASSWORD=contraseña
DB_NAME=uci_db
SECRET_KEY=your_secret_key
```

## Inicialización de la base de datos

```bash
python db_init.py
```

## Ejecución

Iniciar el servidor:

```bash
python app.py
```

Por defecto, la API estará disponible en:

```text
http://localhost:5000
```

## Endpoints

Las rutas de la API se encuentran organizadas dentro de la carpeta:

```text
routes/
```

## Autor

Ana Sofía Torres Baena

## Licencia

Proyecto desarrollado con fines académicos y de investigación.
