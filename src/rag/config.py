# Copyright 2026 Muhammad Nizwa
# SPDX-License-Identifier: MIT

from functools import lru_cache

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    # application metadata
    app_name: str = "arXiv co-work"
    app_summary: str = "retrieval agent for long running paper curation"

    debug: str = True


@lru_cache
def get_settings():
    return AppSettings()
