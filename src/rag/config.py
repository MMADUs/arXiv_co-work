# Copyright 2026 Muhammad Nizwa
# SPDX-License-Identifier: MIT

from functools import lru_cache

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class S3Settings(BaseModel):
    endpoint_url: str = Field(description="s3 endpoint url")
    access_key_id: str = Field(description="s3 access key")
    secret_access_key: str = Field(description="s3 secret key")
    region_name: str = "us-east-1"
    bucket_name: str = "arxiv-papers"


class PostgresSettings(BaseModel):
    db_url: str = Field(description="postgres database url")
    echo_sql: bool = False
    pool_size: int = 20
    max_overflow: int = 0


class AppSettings(BaseSettings):
    # application metadata
    app_name: str = "arXiv co-work"
    app_summary: str = "retrieval agent for long running paper curation"

    # debug mode
    debug: bool = True

    # read .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # api settings
    api_prefix: str = "/api"

    postgres: PostgresSettings = Field(default_factory=PostgresSettings)
    s3: S3Settings = Field(default_factory=S3Settings)


@lru_cache
def get_settings():
    return AppSettings()
