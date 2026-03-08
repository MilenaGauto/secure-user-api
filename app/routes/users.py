# Importamos APIRouter para agrupar las rutas, Depends para la BD, y HTTPException para los errores
from fastapi import APIRouter, Depends, HTTPException, status

# Importamos Session para tipar la conexión a la base de datos
from sqlalchemy.orm import Session

# Importamos la conexión local para instanciar la base de datos
from app.database.connection import SessionLocal

# Importamos los servicios que ahora sí hablan con PostgreSQL
from app.services import user_service

# Importamos el esquema de Pydantic para validar los datos de entrada al actualizar
from app.schemas.user_schema import UserCreate

router = APIRouter()

# --- DEPENDENCIA DE BASE DE DATOS ---
def get_db():
    """Genera una sesión de base de datos por cada petición y la cierra al finalizar."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/users", status_code=status.HTTP_200_OK)
def list_users(db: Session = Depends(get_db)):
    """
    Obtiene la lista de todos los usuarios registrados.
    """
    return user_service.get_users(db)


@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un usuario específico por su ID.
    Si el usuario no existe en la base de datos, devuelve un error 404.
    """
    user = user_service.get_user_by_id(db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Usuario no encontrado"
        )
    return user


@router.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def edit_user(user_id: int, user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Actualiza los datos de un usuario existente.
    Recibe los nuevos datos validados por Pydantic (UserCreate).
    """
    # Convertimos el modelo de Pydantic a un diccionario usando .model_dump() (o .dict() en versiones viejas)
    updated_user = user_service.update_user(db, user_id=user_id, user_data=user_data.model_dump())
    
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Usuario no encontrado para actualizar"
        )
    return updated_user


@router.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def remove_user(user_id: int, db: Session = Depends(get_db)):
    """
    Elimina un usuario de la base de datos de forma permanente.
    """
    success = user_service.delete_user(db, user_id=user_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Usuario no encontrado para eliminar"
        )
    return {"message": f"Usuario con ID {user_id} eliminado exitosamente"}