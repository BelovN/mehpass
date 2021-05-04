# stdlib
from typing import List

# fastapi
from fastapi import Depends
from fastapi.exceptions import HTTPException

# project
from starlette import status

from crypto.models.passwords import PasswordCreate, PasswordUpdate
from crypto import tables as crypto_tables
from mehpass.database import Session, get_session


class PasswordsManager:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, user_id: int) -> List[crypto_tables.Password]:
        passwords = (
            self.session.query(crypto_tables.Password).filter_by(user_id=user_id).all()
        )
        return passwords

    def __get(self, user_id: int, password_id: int) -> crypto_tables.Password:
        password = (
            self.session.query(crypto_tables.Password)
            .filter_by(id=password_id, user_id=user_id)
            .first()
        )
        if not password:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return password

    def get(self, user_id: int, password_id: int) -> crypto_tables.Password:
        return self.__get(user_id, password_id)

    def create(
        self, user_id: int, password_data: PasswordCreate
    ) -> crypto_tables.Password:
        password = crypto_tables.Password(user_id=user_id, **password_data.dict())
        self.session.add(password)
        self.session.commit()
        return password

    def update(
        self, user_id: int, password_id: int, password_data: PasswordUpdate
    ) -> crypto_tables.Password:

        password = self.__get(user_id, password_id)
        for field, value in password_data:
            setattr(password, field, value)
        self.session.commit()
        return password

    def delete(self, user_id: int, password_id: int) -> None:
        password = self.__get(user_id, password_id)
        self.session.delete(password)
        self.session.commit()
