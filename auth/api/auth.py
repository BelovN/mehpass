# fastapi
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

# app
from auth.api.models.auth import Token, UserCreate
from auth.api.controllers import AuthController


router = APIRouter(prefix="/auth")


@router.post("/sign-up", response_model=Token)
def sign_up(user_data: UserCreate, service: AuthController = Depends()):
    return service.register(user_data)


@router.post("/sign-in", response_model=Token)
def sign_in(
    form_data: OAuth2PasswordRequestForm = Depends(), service: AuthController = Depends()
):
    return service.authenticate(
        username=form_data.username, password=form_data.password
    )
