# Importamos tipos de columnas de SQLAlchemy
# Column define una columna en la base de datos
# Integer y String son tipos de datos
from sqlalchemy import Column, Integer, String

# Importamos la clase Base que definimos en la conexión a la base de datos
# Todos los modelos deben heredar de Base
from app.database.connection import Base


# Creamos el modelo User
# Esta clase representa la tabla "users" en PostgreSQL
class User(Base):

    # Nombre de la tabla en la base de datos
    __tablename__ = "users"


    # Columna ID
    # Integer -> número entero
    # primary_key=True -> clave primaria
    # index=True -> crea un índice para búsquedas más rápidas
    id = Column(Integer, primary_key=True, index=True)


    # Columna username
    # String -> texto
    # unique=True -> no puede repetirse
    # index=True -> mejora las búsquedas
    username = Column(String, unique=True, index=True)


    # Columna email
    # También es única para evitar usuarios duplicados
    email = Column(String, unique=True, index=True)


    # Columna password
    # Aquí se guarda la contraseña hasheada (nunca en texto plano)
    password = Column(String)