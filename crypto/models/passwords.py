# stdlib
from datetime import date

# thirdparty
from pydantic import BaseModel


class PasswordBase(BaseModel):
    last_update: date
    service_name: str
    login_hash: str
    password_hash: str


class Password(PasswordBase):
    id: int

    class Config:
        orm_mode = True


class PasswordCreate(PasswordBase):
    pass


class PasswordUpdate(PasswordBase):
    pass
