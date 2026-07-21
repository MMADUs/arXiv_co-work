# Copyright 2026 Muhammad Nizwa
# SPDX-License-Identifier: MIT

import logging

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from rag import __version__
from rag.config import get_settings

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    config = get_settings()

    app.state.config = config

    logger.info("Application startup completed")

    try:
        yield
    finally:
        logger.info("Application shutdown completed")


def create_app() -> FastAPI:
    config = get_settings()

    app = FastAPI(
        title=config.app_name,
        summary=config.app_summary,
        # description=...,
        version=__version__,
        debug=config.debug,
        # docs_url=...,
        # redoc_url=...,
        # openapi_url=...,
        # openapi_tags=...,
        # swagger_ui_parameters=...,
        # contact=...,
        # license_info=...,
        # servers=...,
        lifespan=lifespan,
    )

    return app


app = create_app()
