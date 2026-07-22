# Copyright 2026 Muhammad Nizwa
# SPDX-License-Identifier: MIT

from collections.abc import Generator
from contextlib import contextmanager

from fastapi import Request
from sqlalchemy.orm import Session

from rag.config import AppSettings, get_settings
from rag.db.config.interface import BaseDatabase
from rag.db.config.factory import create_database

_global_db_session: BaseDatabase | None = None


def get_db_session(request: Request) -> Generator[Session, None, None]:
    """
    FastAPI dependency for db session
    """
    database: BaseDatabase | None = getattr(request.app.state, "database", None)

    if database is None:
        raise RuntimeError("Database is not initialized on app.state")

    with database.get_session() as session:
        yield session


@contextmanager
def use_db_session(
    settings: AppSettings | None = None,
) -> Generator[Session, None, None]:
    """
    session helper for scripts that requires one time session
    """
    global _global_db_session

    if _global_db_session is None:
        _global_db_session = create_database(settings or get_settings())
        _global_db_session.startup()

    with _global_db_session.get_session() as session:
        yield session
