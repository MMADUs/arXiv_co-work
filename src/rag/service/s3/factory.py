# Copyright 2026 Muhammad Nizwa
# SPDX-License-Identifier: MIT

from rag.config import AppSettings, get_settings
from rag.service.s3.interface import BaseStorage
from rag.service.s3.s3_storage import S3Storage


def create_s3_storage(settings: AppSettings | None = None) -> BaseStorage:
    settings = settings or get_settings()

    return S3Storage(settings.s3_settings)
