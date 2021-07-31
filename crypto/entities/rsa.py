from __future__ import annotations


from dataclasses import dataclass


@dataclass
class KeyEntity:
    key: bytes


@dataclass
class RSAPublicKeyEntity(KeyEntity):
    pass


@dataclass
class RSAPrivateKeyEntity(KeyEntity):
    pass


@dataclass
class RSAKeysEntity:
    public_key: RSAPublicKeyEntity
    private_key: RSAPrivateKeyEntity

    @classmethod
    def from_keys(cls, public_key: bytes, private_key: bytes) -> RSAKeysEntity:
        """Собрать Entity из ключей"""

        public_key_entity = RSAPublicKeyEntity(public_key)
        private_key_entity = RSAPrivateKeyEntity(private_key)

        return cls(public_key=public_key_entity, private_key=private_key_entity)
