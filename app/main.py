from fastapi import FastAPI
from app.database.connection import Base, engine
from app.models.user import User
from app.routes.auth import router as auth_router

app = FastAPI()

# Crear tablas en PostgreSQL
Base.metadata.create_all(bind=engine)

# Registrar rutas de auth
app.include_router(auth_router, prefix="/auth", tags=["Auth"])