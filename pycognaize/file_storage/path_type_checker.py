from pathlib import Path
from typing import Union

from cloudpathlib import AnyPath, S3Path


def get_path_from_string(path: str) -> Path:
    return AnyPath(path)


def is_local_path(path: Union[str, Path]) -> bool:
    if isinstance(path, str):
        path = get_path_from_string(path)

    return isinstance(path, Path)


def is_s3_path(path: Union[str, Path]) -> bool:
    if isinstance(path, str):
        path = get_path_from_string(path)

    return isinstance(path, S3Path)
