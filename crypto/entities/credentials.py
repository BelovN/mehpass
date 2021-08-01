# thirdparty
from pydantic import BaseModel

# project
from .base import DateInfoMixin


class ServiceInfoMixin(BaseModel):
    service_name: str
    url: str


class CredentialsBase(DateInfoMixin, ServiceInfoMixin):
    login: str
    password: str
