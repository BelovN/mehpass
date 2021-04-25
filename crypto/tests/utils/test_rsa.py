import pytest

from crypto.services.rsa import encrypt, decrypt, generate_random_rsa_keys


def test_generate_key():
    pubkey, seckey = generate_random_rsa_keys()
    assert pubkey
    assert seckey
    assert pubkey != seckey


@pytest.fixture
def rsa_key():
    return generate_random_rsa_keys()


@pytest.fixture
def message():
    msg = "Encrypt this message".encode()
    return msg


def test_encrypt_decrypt(message, rsa_key):
    pubkey, seckey = rsa_key
    encrypted = encrypt(pubkey, message)
    decrypted = decrypt(seckey, encrypted)

    assert encrypted != decrypted
    assert decrypted == message
