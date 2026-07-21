# Copyright 2026 Muhammad Nizwa
# SPDX-License-Identifier: MIT

import logging

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from rag import __version__
from rag.config import get_settings

from rag.routes.health import router as health_router

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
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        summary=settings.app_summary,
        # description=...,
        version=__version__,
        debug=settings.debug,
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

    app.include_router(router=health_router, prefix=settings.api_prefix)

    return app


app = create_app()
