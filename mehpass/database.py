# thirdparty
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# project
from .settings import settings


engine = create_engine(
    settings.database_url, connect_args={"check_same_thread": False},
)

Session = sessionmaker(engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
