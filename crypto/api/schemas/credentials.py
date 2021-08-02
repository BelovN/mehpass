# project
from crypto.services.entities.credentials import CredentialsBase


class CredentialSchema(CredentialsBase):
    id: int

    class Config:
        orm_mode = True


class CredentialCreateSchema(CredentialsBase):
    pass


class CredentialUpdateSchema(CredentialsBase):
    pass
