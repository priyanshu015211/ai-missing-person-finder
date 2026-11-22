from collections.abc import Generator
from functools import lru_cache

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings


@lru_cache(maxsize=1)
def get_engine() -> Engine:
    """Create the shared engine on first database use, not at API import time."""
    return create_engine(
        settings.database_url,
        pool_pre_ping=True,
        pool_recycle=1800,
        connect_args={"connect_timeout": 5},
    )


@lru_cache(maxsize=1)
def get_session_factory() -> sessionmaker[Session]:
    return sessionmaker(
        bind=get_engine(),
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
    )


def get_db() -> Generator[Session, None, None]:
    """Yield a SQLAlchemy session and always close it after the request."""
    db = get_session_factory()()
    try:
        yield db
    finally:
        db.close()


def check_database_connection() -> None:
    """Raise a SQLAlchemy exception if MySQL cannot execute a trivial query."""
    with get_engine().connect() as connection:
        connection.execute(text("SELECT 1"))
