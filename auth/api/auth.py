# fastapi
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

# app
from auth.models.auth import Token, UserCreate
from auth.services.auth import AuthService


router = APIRouter(prefix="/auth")


@router.post("/sign-up", response_model=Token)
def sign_up(user_data: UserCreate, service: AuthService = Depends()):
    return service.register_new_user(user_data)


@router.post("/sign-in", response_model=Token)
def sign_in(
    form_data: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends()
):
    return service.authenticate_user(
        username=form_data.username, password=form_data.password
    )
