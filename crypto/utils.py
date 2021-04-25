"""Модель для общих алгоритмов."""

# stdlib
from hashlib import sha256


def hash_keyword(key_word):
    """Получает хеш из ключевого слова."""
    key_bytes = key_word.encode()
    key_hash = sha256(key_bytes).digest()
    return key_hash
