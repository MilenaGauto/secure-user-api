# Importamos create_engine para crear la conexión con la base de datos
from sqlalchemy import create_engine

# Importamos herramientas del ORM
# sessionmaker: crea sesiones para interactuar con la base de datos
# declarative_base: permite definir modelos como clases de Python
from sqlalchemy.orm import sessionmaker, declarative_base


# URL de conexión a la base de datos PostgreSQL
# Formato:
# postgresql://usuario:password@host:puerto/nombre_db
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/secure_user_api"


# Engine es el objeto que maneja la conexión con la base de datos
# SQLAlchemy lo usa para ejecutar consultas
engine = create_engine(DATABASE_URL)


# SessionLocal es una "fábrica de sesiones"
# Cada vez que la API necesita acceder a la base de datos
# crea una sesión usando este objeto
SessionLocal = sessionmaker(

    # autocommit=False significa que debemos confirmar manualmente los cambios
    autocommit=False,

    # autoflush=False evita que SQLAlchemy envíe cambios automáticamente
    autoflush=False,

    # bind conecta la sesión con el engine de la base de datos
    bind=engine
)


# Base es la clase base que usarán todos los modelos de la base de datos
# Cada modelo heredará de Base
# Ejemplo: class User(Base)
Base = declarative_base()