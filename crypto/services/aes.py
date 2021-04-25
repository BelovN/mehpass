"""Модуль для шифрования в AES."""

# thirsty
from Crypto.Cipher import AES


def encrypt(msg, key_hash):  # TODO: TypeHints
    """Кодирование сообщения с помощью хеша-ключа."""
    cipher = AES.new(key_hash, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg)
    return nonce, ciphertext, tag


def decrypt(nonce, ciphertext, tag, key_hash):  # TODO: TypeHints
    """Декодирование сообщения с помощью хеша-ключа."""
    cipher = AES.new(key_hash, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext
    finally:
        return False
