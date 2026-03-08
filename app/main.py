# Importamos FastAPI
from fastapi import FastAPI

# Importamos la configuración de la base de datos
from app.database.connection import Base, engine

# Importamos los routers que construimos
from app.routes.auth import router as auth_router
from app.routes.users import router as users_router

# Inicializamos la aplicación con metadatos para la documentación
app = FastAPI(
    title="Secure User API",
    description="API REST segura para gestión y autenticación de usuarios",
    version="1.0.0"
)

# Esto crea las tablas en PostgreSQL si no existen.
# Nota: En proyectos más grandes, esta línea se reemplaza por migraciones con Alembic.
Base.metadata.create_all(bind=engine)

# Registramos el router de autenticación (Login y Registro)
# El prefix="/auth" hace que todas las rutas empiecen con ese prefijo
app.include_router(auth_router, prefix="/auth", tags=["Autenticación"])

# Registramos el router de gestión de usuarios (CRUD)
# Acá no usamos prefix para que las rutas queden directamente como /users
app.include_router(users_router, tags=["Gestión de Usuarios"])