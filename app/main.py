from fastapi import FastAPI
from app.routes.users import router as user_router
from app.routes.auth import router as auth_router

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)