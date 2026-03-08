# Importamos BaseModel desde Pydantic
# BaseModel permite crear modelos para validar datos de entrada
from pydantic import BaseModel


# Creamos un schema llamado UserCreate
# Este modelo define los datos que el usuario debe enviar al registrarse
class UserCreate(BaseModel):

    # Campo email
    # FastAPI espera un string en este campo
    email: str

    # Campo password
    # También espera un string
    password: str