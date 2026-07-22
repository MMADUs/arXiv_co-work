# Copyright 2026 Muhammad Nizwa
# SPDX-License-Identifier: MIT

import json
import logging
from pathlib import Path
from typing import Any

import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

from rag.config import S3Settings

logger = logging.getLogger(__name__)


class S3Client:
    """
    S3 Object Storage Client interface
    """

    def __init__(self, settings: S3Settings) -> None:
        self.settings = settings
        self.client = boto3.client(
            "s3",
            endpoint_url=self.settings.endpoint_url,
            aws_access_key_id=self.settings.access_key_id,
            aws_secret_access_key=self.settings.secret_access_key,
            region_name=self.settings.region_name,
            config=Config(
                signature_version="s3v4",
                s3={"addressing_style": "path"},
                connect_timeout=5,
                read_timeout=30,
                retries={
                    "max_attempts": 3,
                    "mode": "standard",
                },
            ),
        )
        logger.info("S3 client initialized")

    def ensure_bucket_exists(self) -> None:
        try:
            self.client.head_bucket(Bucket=self.settings.bucket_name)
            return

        except ClientError as error:
            status_code = error.response["ResponseMetadata"]["HTTPStatusCode"]

            if status_code != 404:
                raise RuntimeError(f"Failed to access S3 bucket: {error}")

        self.client.create_bucket(Bucket=self.settings.bucket_name)

    def close(self) -> None:
        self.client.close()

    def upload_file(self, local_path: Path, object_key: str) -> None:
        self.ensure_bucket_exists()

        self.client.upload_file(
            Filename=str(local_path),
            Bucket=self.settings.bucket_name,
            Key=object_key,
        )

    def download_file(self, local_path: Path, object_key: str) -> None:
        local_path.parent.mkdir(parents=True, exist_ok=True)

        self.client.download_file(
            Filename=str(local_path),
            Bucket=self.settings.bucket_name,
            Key=object_key,
        )

    def upload_json(self, data: dict[str, Any], object_key: str) -> None:
        self.ensure_bucket_exists()

        self.client.put_object(
            Bucket=self.settings.bucket_name,
            Key=object_key,
            Body=json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8"),
            ContentType="application/json",
        )

    def download_json(self, object_key: str) -> dict[str, Any]:
        response = self.client.get_object(
            Bucket=self.settings.bucket_name,
            Key=object_key,
        )

        body = response["Body"].read().decode("utf-8")
        return json.loads(body)
