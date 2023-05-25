from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.config import settings

engine = create_engine(settings.POSTGRES_URI, echo=True, pool_pre_ping=True)

session_class = sessionmaker(
    autocommit=False, autoflush=True, bind=engine, expire_on_commit=False, class_=Session
)


def get_session():
    with session_class() as session:
        yield session
