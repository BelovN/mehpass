# thirdparty
from faker import Faker

# app
from crypto.entities.rsa import RSAPublicKeyEntity, RSAPrivateKeyEntity, RSAKeysEntity
from crypto.services.rsa import RSAManager

fake = Faker()


class TestRSAManager:
    def test_generate_key(self):
        rsa_keys = RSAManager.generate_random_rsa_keys()

        assert type(rsa_keys) is RSAKeysEntity
        assert type(rsa_keys.public_key) is RSAPublicKeyEntity
        assert type(rsa_keys.private_key) is RSAPrivateKeyEntity

    def test_encrypt_decrypt(self):
        rsa_keys = RSAManager.generate_random_rsa_keys()

        message = fake.pystr()

        encrypted = RSAManager.encrypt(rsa_keys.public_key, message)
        decrypted = RSAManager.decrypt(rsa_keys.private_key, encrypted)

        assert encrypted != decrypted
        assert decrypted == message
