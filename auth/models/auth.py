# thirdparty
from pydantic import BaseModel, ValidationError, validator


from ..services.validators import get_pwd_validator, get_username_validator, PWD_ERROR_MSG


class BaseUser(BaseModel):
    username: str


class UserCreate(BaseUser):
    password: str

    @validator("username")
    def validate_username(cls, value):
        get_username_validator().validate_all(value)

    @validator("password")
    def validate_password(cls, value):
        if not get_pwd_validator().validate(value):
            raise ValidationError(PWD_ERROR_MSG)


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
