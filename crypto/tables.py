import sqlalchemy as sa
from sqlalchemy.orm import relationship

from auth.tables import User
from mehpass.database import Base


class Password(Base):
    __tablename__ = "passwords"

    id = sa.Column(sa.Integer, primary_key=True, unique=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    last_update = sa.Column(sa.Date)
    service_name = sa.Column(sa.String)
    login_hash = sa.Column(sa.String)
    password_hash = sa.Column(sa.String)

    user = relationship(User)
