# thirdparty
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# project
from crypto.services.entities.rsa import RSAKeysEntity, RSAPrivateKeyEntity, RSAPublicKeyEntity


class RSAManager:
    encoding: str = "utf-8"

    @classmethod
    def generate_random_rsa_keys(cls, bits: int = 1024) -> RSAKeysEntity:
        """Создаем случайные RSA ключи."""
        random_generator = Random.new().read
        rsa_key = RSA.generate(bits, random_generator)

        return RSAKeysEntity.from_keys(
            private_key=rsa_key.exportKey(), public_key=rsa_key.public_key().exportKey()
        )

    @classmethod
    def encrypt(cls, public_key: RSAPublicKeyEntity, message: str) -> bytes:
        """Кодирование в RSA c помощью публичного ключа."""
        key = RSA.importKey(public_key.key)
        cipher = PKCS1_OAEP.new(key)

        # => Конвертируем в байты
        message_bytes = bytes(message, encoding=cls.encoding)

        encrypted = cipher.encrypt(message_bytes)
        return encrypted

    @classmethod
    def decrypt(cls, private_key: RSAPrivateKeyEntity, encrypted: bytes) -> str:
        """Декодирование из RSA c помощью приватного ключа."""

        # => Импортируем ключ
        rsa_key = RSA.importKey(private_key.key)
        cipher = PKCS1_OAEP.new(rsa_key)

        # => Расшифровываем
        decrypted = cipher.decrypt(encrypted)

        return decrypted.decode(cls.encoding)
