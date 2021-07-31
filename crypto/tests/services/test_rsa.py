# thirdparty
import pytest

# app
from crypto.services.rsa import RSAManager


class TestRSAManager:
    @pytest.fixture
    def test_rsa_key(self):
        return RSAManager.generate_random_rsa_keys()

    @pytest.fixture
    def message(self):
        msg = "Encrypt this message".encode()
        return msg

    def test_generate_key(self):
        pubkey, seckey = RSAManager.generate_random_rsa_keys()
        assert pubkey
        assert seckey
        assert pubkey != seckey

    def test_encrypt_decrypt(self, message, rsa_key):
        pubkey, seckey = rsa_key
        encrypted = RSAManager.encrypt(pubkey, message)
        decrypted = RSAManager.decrypt(seckey, encrypted)

        assert encrypted != decrypted
        assert decrypted == message
