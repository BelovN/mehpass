# thirdparty
from password_validator import PasswordValidator
from username_validator import UsernameValidator

_MIN_COUNT_SYMBOLS: int = 8
_MAX_COUNT_SYMBOLS: int = 50

PWD_ERROR_MSG: str = "Password must include from {} to {} symbols, uppercase and lowercase, digits. " "Must not include spaces.".format(
    _MIN_COUNT_SYMBOLS, _MAX_COUNT_SYMBOLS
)


def _setup_validator(pwd_validator: PasswordValidator) -> None:
    """Настройка валидации пароля"""
    pwd_validator.min(_MIN_COUNT_SYMBOLS).max(
        _MAX_COUNT_SYMBOLS
    ).has().uppercase().has().lowercase().has().digits().has().no().spaces()


def get_pwd_validator() -> PasswordValidator:
    """Получение валидатора пароля"""
    pwd_validator = PasswordValidator()
    _setup_validator(pwd_validator)
    return pwd_validator


def get_username_validator() -> UsernameValidator:
    """Получение валидатора имени пользователя"""
    return UsernameValidator()
