# Secure User API

API REST segura para gestión de usuarios con autenticación JWT construida con **FastAPI**.

## 🚀 Features

* Registro de usuarios
* Autenticación con JWT
* Hash seguro de contraseñas
* CRUD de usuarios
* Estructura profesional por capas
* Documentación automática con Swagger

## 🛠️ Tecnologías

* FastAPI
* Python
* JWT (python-jose)
* Passlib (bcrypt)
* Uvicorn

## 📂 Estructura del proyecto

```
secure-user-api
│
├── app
│   ├── main.py
│   ├── models
│   │   └── user.py
│   ├── schemas
│   │   └── user_schema.py
│   ├── routes
│   │   └── user_routes.py
│   ├── services
│   │   ├── auth_service.py
│   │   └── user_service.py
│   └── utils
│       └── security.py
│
├── requirements.txt
└── README.md
```

## ▶️ Ejecutar el proyecto

Instalar dependencias:

```
pip install -r requirements.txt
```

Correr el servidor:

```
uvicorn app.main:app --reload
```

## 📖 Documentación de la API

Swagger UI:

```
http://127.0.0.1:8000/docs
```

## 🔐 Endpoints principales

| Método | Endpoint    | Descripción           |
| ------ | ----------- | --------------------- |
| POST   | /register   | Registrar usuario     |
| POST   | /login      | Login y obtener token |
| GET    | /users      | Listar usuarios       |
| GET    | /users/{id} | Obtener usuario       |
| DELETE | /users/{id} | Eliminar usuario      |

## 👨‍💻 Autor

Proyecto backend desarrollado para práctica profesional con FastAPI.
