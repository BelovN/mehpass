# stdlib
from typing import List

# project
from crypto import tables as crypto_tables
from crypto.api.schemas.credentials import CredentialCreateSchema, CredentialUpdateSchema

# fastapi
from fastapi import Depends
from fastapi.exceptions import HTTPException
from mehpass.database import Session, get_session

# thirdparty
from starlette import status


class CredentialService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, user_id: int) -> List[crypto_tables.Password]:
        """Получение списка данных для входа из БД"""
        passwords = (
            self.session.query(crypto_tables.Password).filter_by(user_id=user_id).all()
        )
        return passwords

    def __get(self, user_id: int, password_id: int) -> crypto_tables.Password:
        """Получение записи данных для входа из БД"""
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
        self, user_id: int, password_data: CredentialCreateSchema
    ) -> crypto_tables.Password:
        """Создание записи в БД для данных входа"""

        password = crypto_tables.Password(user_id=user_id, **password_data.dict())
        self.session.add(password)
        self.session.commit()
        return password

    def update(
        self, user_id: int, password_id: int, password_data: CredentialUpdateSchema
    ) -> crypto_tables.Password:
        """Обновление данных для входа в БД"""

        password = self.__get(user_id, password_id)
        for field, value in password_data:
            setattr(password, field, value)
        self.session.commit()
        return password

    def delete(self, user_id: int, password_id: int) -> None:
        """Удаление записи из БД"""

        password = self.__get(user_id, password_id)
        self.session.delete(password)
        self.session.commit()
