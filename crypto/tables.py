import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Password(Base):
    __tablename__ = "passwords"

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.Date)
    service_name = sa.Column(sa.String)
