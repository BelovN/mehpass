# stdlib
from dataclasses import dataclass
from datetime import datetime


@dataclass
class DateInfoMixin:
    created_at: datetime
    last_update: datetime


@dataclass
class ServiceInfoMixin:
    service_name: str
    url: str


@dataclass
class CredentialsBase(DateInfoMixin, ServiceInfoMixin):
    login: str
    password: str
