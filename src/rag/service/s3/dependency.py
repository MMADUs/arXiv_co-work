# Copyright 2026 Muhammad Nizwa
# SPDX-License-Identifier: MIT

from fastapi import Request

from rag.service.s3.interface import BaseStorage


def get_s3_storage(request: Request) -> BaseStorage:
    """
    FastAPI dependency for object storage
    """
    storage: BaseStorage | None = getattr(request.app.state, "s3_storage", None)

    if storage is None:
        raise RuntimeError("S3 storage is not initialized on app.state")

    return storage