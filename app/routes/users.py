# Importa APIRouter de FastAPI para crear rutas agrupadas
from fastapi import APIRouter

# Importa el modelo de usuario que define la estructura de los datos
from app.models.user import User

# Importa las funciones de lógica de negocio desde user_service
from app.services.user_service import (
    get_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user
)

# Crea un router para agrupar las rutas relacionadas con usuarios
router = APIRouter()

# Endpoint para obtener todos los usuarios
@router.get("/users")
def list_users():
    # Llama al servicio que devuelve la lista de usuarios
    return get_users()


# Endpoint para obtener un usuario por su ID
@router.get("/users/{user_id}")
def get_user(user_id: int):
    # user_id se recibe desde la URL
    return get_user_by_id(user_id)


# Endpoint para crear un nuevo usuario
@router.post("/users")
def add_user(user: User):
    # FastAPI valida automáticamente el JSON usando el modelo User
    return create_user(user)


# Endpoint para actualizar un usuario existente
@router.put("/users/{user_id}")
def edit_user(user_id: int, user: User):
    # Actualiza el usuario con el ID especificado
    return update_user(user_id, user)


# Endpoint para eliminar un usuario
@router.delete("/users/{user_id}")
def remove_user(user_id: int):
    # Elimina el usuario con el ID especificado
    return delete_user(user_id)