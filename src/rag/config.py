# Copyright 2026 Muhammad Nizwa
# SPDX-License-Identifier: MIT

from functools import lru_cache

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    # application metadata
    app_name: str = "arXiv co-work"
    app_summary: str = "retrieval agent for long running paper curation"

    # debug mode
    debug: bool = True

    # read .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # api settings
    api_prefix: str = "/api"


@lru_cache
def get_settings():
    return AppSettings()
