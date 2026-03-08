from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.services.user_service import create_user, get_user_by_email
from app.services.auth_service import verify_password, create_access_token
from app.services.auth_service import hash_password

router = APIRouter()


@router.post("/register")
def register(user: User):

    user.password = hash_password(user.password)

    create_user(user)

    return {"message": "User registered"}

@router.post("/login")
def login(email: str, password: str):

    user = get_user_by_email(email)

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    token = create_access_token({"sub": user.email})

    return {"access_token": token}