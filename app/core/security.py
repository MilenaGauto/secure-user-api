# Importamos CryptContext para manejar el hashing de contraseñas de forma segura
from passlib.context import CryptContext

# Librerías para manejar el tiempo de expiración del token con zonas horarias
from datetime import datetime, timedelta, timezone

# Librería para crear y firmar JSON Web Tokens (JWT)
from jose import jwt


# Clave secreta usada para firmar los tokens JWT.
# NOTA DE SEGURIDAD: En producción, esto DEBE venir de un archivo .env
SECRET_KEY = "secret"

# Algoritmo criptográfico usado para firmar el token
ALGORITHM = "HS256"

# Tiempo de expiración del token (en minutos) para mitigar ataques de interceptación
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# Creamos el contexto de hashing indicando que usaremos bcrypt (estándar de la industria)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Convierte una contraseña en texto plano a un hash seguro usando bcrypt
    antes de guardarla en PostgreSQL.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Compara la contraseña en texto plano ingresada en el login con el hash 
    guardado en la base de datos.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """
    Genera un JSON Web Token (JWT) firmado para la autenticación del usuario.
    """
    # Copiamos los datos para no modificar el diccionario original
    to_encode = data.copy()

    # Calculamos cuándo expira el token usando la zona horaria UTC (buena práctica actual)
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Agregamos la fecha de expiración ('exp') al payload del token
    to_encode.update({"exp": expire})

    # Generamos el token firmado usando nuestra clave secreta y algoritmo
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    # Devolvemos el string del token
    return encoded_jwt