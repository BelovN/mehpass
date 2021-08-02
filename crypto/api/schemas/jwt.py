# stdlib
from datetime import datetime

# thirdparty
from pydantic import BaseModel

# project
from auth.api.schemas.auth import UserSchema


class JWTSchema(BaseModel):
    iat: datetime
    nbf: datetime
    exp: datetime
    sub: str
    user: UserSchema
