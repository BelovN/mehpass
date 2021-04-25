import sqlalchemy as sa
from mehpass.database import Base


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, unique=True)
    ass = sa.Column(sa.String)
    username = sa.Column(sa.String, unique=True)
    password = sa.Column(sa.String)
