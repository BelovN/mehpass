# stdlib
from datetime import datetime

# thirdparty
from pydantic import BaseModel


class DateInfoMixin(BaseModel):
    created_at: datetime
    last_update: datetime

