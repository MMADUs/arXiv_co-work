# Copyright 2026 Muhammad Nizwa
# SPDX-License-Identifier: MIT

from typing import Protocol
from pathlib import Path


class BaseStorage(Protocol):
    """
    Any object storage providers must implement the methods defined here,
    but do not need to inherit from BaseStorage
    """

    def ensure_bucket_exists(self) -> None:
        """
        inspect bucket if exist, otherwise create new bucket
        """
        ...

    def close(self) -> None:
        """
        close client connection from storage
        """
        ...

    def upload_file(self, local_path: Path, object_key: str) -> None:
        """
        upload object to storage
        """
        ...

    def download_file(self, local_path: Path, object_key: str) -> None:
        """
        download object from storage
        """
        ...
