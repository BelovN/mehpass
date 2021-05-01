# thirdparty
import pytest

# app
from crypto.services.aes import encrypt, decrypt
from crypto.utils import hash_keyword


@pytest.fixture
def message():
    msg = b"\x97<A\x01\xe4S\x05\xf2o\xa5\x08\x0e\x9c\x07\x10e\x97<A\x01\xe4S\x05\xf2o\xa5\x08\x0e\x9c\x07\x10e"
    return msg


@pytest.fixture
def key_word():
    hash = hash_keyword("mypasswd")
    return hash


def test_encrypt_decrypt(message, key_word):
    nonce, ciphertext, tag = encrypt(message, key_word)
    decrypted = decrypt(nonce, ciphertext, tag, key_word)

    assert message == decrypted
