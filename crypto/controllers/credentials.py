# stdlib
from typing import List

# fastapi
from fastapi import APIRouter, Depends, Response

# project
from starlette import status

from auth.services.auth import get_current_user
from auth.tables import User

# app
from crypto.models.credentials import Password, PasswordCreate, PasswordUpdate
from crypto.services.credentials import CredentialService


router = APIRouter(prefix="/passwords")


@router.get("/", response_model=List[Password])
def get_passwords(
    service: CredentialService = Depends(), user: User = Depends(get_current_user)
):
    passwords = service.get_list(user_id=user.id)
    return passwords


@router.get("/{password_id}", response_model=Password)
def get_password(
    password_id: int,
    service: CredentialService = Depends(),
    user: User = Depends(get_current_user),
):
    return service.get(user_id=user.id, password_id=password_id)


@router.put("/", response_model=Password)
def create_password(
    password_data: PasswordCreate,
    service: CredentialService = Depends(),
    user: User = Depends(get_current_user),
):
    return service.create(user_id=user.id, password_data=password_data)


@router.post("/{password_id}", response_model=Password)
def update_password(
    password_id: int,
    password_data: PasswordUpdate,
    service: CredentialService = Depends(),
    user: User = Depends(get_current_user),
):
    return service.update(
        user_id=user.id, password_data=password_data, password_id=password_id
    )


@router.delete("/{password_id}")
def delete_password(
    password_id: int,
    service: CredentialService = Depends(),
    user: User = Depends(get_current_user),
):
    service.delete(password_id=password_id, user_id=user.id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
