# fastapi
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

# app
from auth.api.schemas.auth import TokenSchema, UserCreateSchema
from auth.api.controllers.auth import AuthController


router = APIRouter(prefix="/auth")


@router.post("/sign-up", response_model=TokenSchema)
def sign_up(user_data: UserCreateSchema, service: AuthController = Depends()):
    return service.register(user_data)


@router.post("/sign-in", response_model=TokenSchema)
def sign_in(
    form_data: OAuth2PasswordRequestForm = Depends(), service: AuthController = Depends()
):
    return service.authenticate(
        username=form_data.username, password=form_data.password
    )
