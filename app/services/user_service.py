# Importamos Session de SQLAlchemy para poder tipar y manejar la conexión a la base de datos
from sqlalchemy.orm import Session

# Importamos el modelo User que mapea exactamente cómo es la tabla en PostgreSQL
from app.models.user import User

# Importamos el esquema (Pydantic) para tener autocompletado y validación de los datos de entrada
from app.schemas.user_schema import UserCreate


def get_users(db: Session):
    """
    Obtiene la lista de todos los usuarios registrados en la base de datos.
    """
    # db.query(User) prepara la consulta SELECT * FROM users
    # .all() ejecuta la consulta y devuelve todos los registros como una lista de objetos
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    """
    Busca un usuario específico utilizando su ID único.
    """
    # .filter() agrega la condición WHERE id = user_id
    # .first() devuelve el primer resultado que encuentre, o None si no existe
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """
    Busca un usuario específico utilizando su correo electrónico.
    Muy útil para el proceso de Login y para verificar que no haya emails duplicados.
    """
    # Funciona igual que la búsqueda por ID, pero filtrando por la columna email
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate, hashed_password: str):
    """
    Crea un nuevo usuario en la base de datos.
    Nota: Recibimos la contraseña ya hasheada desde el auth_service por seguridad.
    """
    # 1. Creamos una instancia del modelo SQLAlchemy con los datos recibidos
    db_user = User(email=user.email, password=hashed_password)
    
    # 2. Agregamos el nuevo objeto a la sesión actual (todavía no se guarda en la BD)
    db.add(db_user)
    
    # 3. Hacemos el "commit" para guardar los cambios permanentemente en PostgreSQL
    db.commit()
    
    # 4. Refrescamos el objeto para que obtenga el ID que le asignó PostgreSQL automáticamente
    db.refresh(db_user)
    
    # Devolvemos el usuario recién creado
    return db_user


def update_user(db: Session, user_id: int, user_data: dict):
    """
    Actualiza los datos de un usuario existente.
    """
    # Primero buscamos si el usuario existe
    db_user = get_user_by_id(db, user_id)
    
    if db_user:
        # Iteramos sobre el diccionario de nuevos datos y actualizamos los atributos
        for key, value in user_data.items():
            setattr(db_user, key, value)
            
        # Guardamos los cambios en la base de datos
        db.commit()
        # Refrescamos para obtener la versión más reciente
        db.refresh(db_user)
        
    return db_user


def delete_user(db: Session, user_id: int):
    """
    Elimina un usuario de la base de datos de forma permanente.
    """
    # Buscamos al usuario que queremos eliminar
    db_user = get_user_by_id(db, user_id)
    
    if db_user:
        # Si existe, lo marcamos para eliminar en la sesión
        db.delete(db_user)
        # Confirmamos la transacción
        db.commit()
        return True
        
    # Si el usuario no existía, devolvemos False
    return False