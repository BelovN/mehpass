# stdlib
from datetime import date

# thirdparty
from pydantic import BaseModel


class Password(BaseModel):
    id: int
    date: date
    service_name: str

    class Config:
        orm_mode = True
