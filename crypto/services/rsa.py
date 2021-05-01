# thirdparty
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def generate_random_rsa_keys():
    """Создаем случайные RSA ключи."""
    random_generator = Random.new().read
    rsa_key = RSA.generate(1024, random_generator)
    return rsa_key.publickey().exportKey(), rsa_key.exportKey()


def encrypt(pubkey, message):  # TODO: TypeHints
    """Кодирование в RSA c помощью публичного ключа."""
    key = RSA.importKey(pubkey)
    cipher = PKCS1_OAEP.new(key)
    encrypted = cipher.encrypt(message)
    return encrypted


def decrypt(seckey, encrypted):  # TODO: TypeHints
    """Декодирование из RSA c помощью приватного ключа."""
    rsa_key = RSA.importKey(seckey)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted = cipher.decrypt(encrypted)
    return decrypted
