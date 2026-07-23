# Copyright 2026 Muhammad Nizwa
# SPDX-License-Identifier: MIT

from rag.config import AppSettings, get_settings
from rag.db.config.interface import BaseDatabase
from rag.db.config.postgresql import PostgreSQLDatabase


def create_database(settings: AppSettings | None = None) -> BaseDatabase:
    settings = settings or get_settings()

    return PostgreSQLDatabase(settings.postgres_settings)
