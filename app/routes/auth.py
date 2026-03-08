# Importamos APIRouter para las rutas, HTTPException para los errores, 
# Depends para la inyección de dependencias y status para los códigos HTTP
from fastapi import APIRouter, HTTPException, Depends, status

# Importamos Session para tipar la conexión a la base de datos
from sqlalchemy.orm import Session

# Importamos el esquema para validar los datos que envía el usuario (body)
from app.schemas.user_schema import UserCreate

# Importamos la lógica de base de datos que armamos en el paso anterior
from app.services import user_service

# Importamos nuestra "caja de herramientas" criptográficas
from app.core import security

# Importamos SessionLocal de tu archivo de conexión para poder abrir la base de datos
from app.database.connection import SessionLocal

router = APIRouter()

# --- DEPENDENCIA DE BASE DE DATOS ---
# Esta función es crucial: abre una sesión con PostgreSQL cada vez que alguien 
# hace una petición a la API, y se asegura de cerrarla cuando la petición termina.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint para registrar un nuevo usuario en el sistema.
    Espera recibir un JSON en el body con 'email' y 'password'.
    """
    # 1. Verificamos si el email ya existe en PostgreSQL
    existing_user = user_service.get_user_by_email(db, email=user.email)
    
    # Si existe, cortamos la ejecución y devolvemos un error 400 (Bad Request)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El email ya está registrado"
        )

    # 2. Hasheamos la contraseña usando nuestro core de seguridad
    hashed_password = security.hash_password(user.password)

    # 3. Guardamos el usuario pasándole la contraseña encriptada (NUNCA en texto plano)
    new_user = user_service.create_user(db=db, user=user, hashed_password=hashed_password)

    # Devolvemos un mensaje de éxito
    return {"message": "Usuario registrado exitosamente", "user_email": new_user.email}


@router.post("/login")
def login(user_credentials: UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint para autenticar a un usuario y devolverle un token JWT.
    También espera recibir un JSON en el body con 'email' y 'password'.
    """
    # 1. Buscamos al usuario en la base de datos por su email
    user = user_service.get_user_by_email(db, email=user_credentials.email)
    
    # 2. Verificamos la identidad:
    # Si el usuario no existe O la contraseña no coincide con el hash guardado...
    if not user or not security.verify_password(user_credentials.password, user.password):
        # Devolvemos error 401 (Unauthorized)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 3. Si pasó las validaciones, generamos el JWT. 
    # El 'sub' (subject) es el estándar para identificar a quién pertenece el token
    access_token = security.create_access_token(data={"sub": user.email})

    # 4. Devolvemos el token en el formato estándar que esperan los clientes web/mobile
    return {"access_token": access_token, "token_type": "bearer"}