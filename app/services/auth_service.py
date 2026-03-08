# Importamos CryptContext para manejar hashing de contraseñas
from passlib.context import CryptContext

# Librerías para manejar tiempo de expiración del token
from datetime import datetime, timedelta

# Librería para crear y firmar JWT
from jose import jwt


# Clave secreta usada para firmar los tokens JWT
# En producción debería estar en variables de entorno
SECRET_KEY = "secret"

# Algoritmo usado para firmar el token
ALGORITHM = "HS256"

# Tiempo de expiración del token (en minutos)
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# Creamos el contexto de hashing
# bcrypt es uno de los algoritmos más seguros para contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Función para hashear una contraseña
# Convierte la contraseña en un hash seguro antes de guardarla en la base de datos
def hash_password(password: str):
    return pwd_context.hash(password)


# Función para verificar contraseña
# Compara la contraseña ingresada con el hash guardado en la base de datos
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# Función para crear un token JWT
def create_access_token(data: dict):

    # Copiamos los datos para no modificar el original
    to_encode = data.copy()

    # Calculamos cuándo expira el token
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Agregamos la fecha de expiración al payload del token
    to_encode.update({"exp": expire})

    # Generamos el token firmado
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    # Devolvemos el token
    return encoded_jwt