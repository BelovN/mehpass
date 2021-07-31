from __future__ import annotations

# stdlib
from dataclasses import dataclass
from datetime import datetime


@dataclass
class CredentialsBase:
    last_update: datetime
    service_name: str
    login: str
    password: str


