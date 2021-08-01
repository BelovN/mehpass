# stdlib
from datetime import datetime, timedelta

# thirdparty
from jose import jwt
from jose.exceptions import JWTError
from passlib.hash import bcrypt
from pydantic import ValidationError

# fastapi
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

# project
from mehpass.database import Session, get_session
from mehpass.settings import settings

# app
from auth import tables
from auth.api.models.auth import User, Token, UserCreate
from auth.api.utils.validators import get_username_validator, get_pwd_validator, PWD_ERROR_MSG

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/sign-in")


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """Обратная зависимоть для проверки аутенификации пользователя"""
    return AuthController.validate_token(token)


class AuthController:
    @classmethod
    def __verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def __hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(
                token, settings.jwt_secret, algorithms=[settings.jwt_algorithm]
            )
        except JWTError:
            raise exception from None

        user_data = payload.get("user")

        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user

    @classmethod
    def __create_token(cls, user: tables.User) -> Token:
        """Создание токена для пользователя"""
        user_data = User.from_orm(user)

        now = datetime.utcnow()
        payload = {
            "iat": now,
            "nbf": now,
            "exp": now + timedelta(seconds=settings.jwt_expiration),
            "sub": str(user_data.id),
            "user": user_data.dict(),
        }
        token = jwt.encode(
            payload, settings.jwt_secret, algorithm=settings.jwt_algorithm
        )
        return Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
        self.username_validator = get_username_validator()
        self.password_validator = get_pwd_validator()

    def register(self, user_data: UserCreate) -> Token:
        """Регистрация нового пользователя"""
        self.__check_user_exists(user_data.username)
        self.__validate_credentials(user_data.username, user_data.password)

        return self.__create_user(
            username=user_data.username, password=user_data.password
        )

    def authenticate(self, username: str, password: str) -> Token:
        """Аутентификация пользователя"""
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        user = self.__get_user(username)

        if not user or not self.__verify_password(password, user.password):
            raise exception

        return self.__create_token(user)

    def __validate_credentials(self, username: str, password: str) -> None:
        """Валидация логина и пароля"""
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            self.username_validator.validate_all(username)
            if not self.password_validator.validate(password):
                raise Exception(PWD_ERROR_MSG)
        except Exception as e:
            exception.detail = str(e)
            raise exception

    def __create_user(self, username: str, password: str) -> Token:
        """Сохранение пользователя в БД"""

        user = tables.User(username=username, password=self.__hash_password(password),)

        self.session.add(user)
        self.session.commit()

        return self.__create_token(user)

    def __get_user(self, username: str) -> tables.User:
        """Получение пользователя"""
        user = (
            self.session.query(tables.User)
            .filter(tables.User.username == username)
            .first()
        )
        return user

    def __check_user_exists(self, username: str) -> None:
        """Проерка существует ли пользователь"""

        user = self.__get_user(username=username)
        if user is not None:
            exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User with name {} already exists!".format(username),
                headers={"WWW-Authenticate": "Bearer"},
            )
            raise exception
