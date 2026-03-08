# Secure User API

REST API for user authentication and management built with **FastAPI**, **PostgreSQL**, and **JWT authentication**.

This project demonstrates a clean backend architecture using **routes, services, schemas, and database layers**.

---

# 🚀 Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT Authentication
* Pydantic
* Uvicorn

---

# 📂 Project Structure

```
app
 ├── database
 │   └── connection.py
 │
 ├── models
 │   └── user.py
 │
 ├── schemas
 │   └── user_schema.py
 │
 ├── routes
 │   ├── auth.py
 │   └── user.py
 │
 ├── services
 │   ├── auth_service.py
 │   └── user_service.py
 │
 └── main.py
```

### Explanation

* **database** → database connection configuration
* **models** → SQLAlchemy database models
* **schemas** → Pydantic validation models
* **routes** → API endpoints
* **services** → business logic
* **main.py** → application entry point

---

# 🔐 Features

* User registration
* User login
* Password hashing
* JWT token generation
* PostgreSQL database integration
* Clean backend architecture

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/MilenaGauto/secure-user-api.git
cd secure-user-api
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# 🗄️ Database Setup

Make sure **PostgreSQL** is installed.

Create the database:

```
CREATE DATABASE secure_user_api;
```

Update the database connection in:

```
app/database/connection.py
```

Example connection string:

```
postgresql://postgres:YOUR_PASSWORD@localhost:5432/secure_user_api
```

---

# ▶️ Running the API

Start the server with:

```
uvicorn app.main:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

---

# 📬 API Endpoints

## Authentication

### Register User

```
POST /auth/register
```

Request example:

```
{
  "email": "user@email.com",
  "password": "123456"
}
```

---

### Login

```
POST /auth/login
```

Request example:

```
{
  "email": "user@email.com",
  "password": "123456"
}
```

Response example:

```
{
  "access_token": "JWT_TOKEN"
}
```

---

# 🔑 Authentication Flow

1. User registers
2. Password is hashed before saving
3. User logs in
4. API generates a JWT token
5. Token can be used to access protected endpoints

---

# 📌 Future Improvements

* Protected routes using JWT
* Docker support
* Database migrations with Alembic
* Refresh tokens
* Role-based authentication

---

# 👩‍💻 Author

Milena Gauto

GitHub
https://github.com/MilenaGauto
