from datetime import datetime
import os
from typing import (
    Dict,
    List,
    Optional
)

from domum.const import (
    DATA_BYTES,
    DATA_KILOBYTES,
    DATA_MEGABYTES,
    DATA_GIGABYTES,
    DATA_TERABYTES
)


class Units:
    DATA_BYTES = 0
    DATA_KILOBYTES = 1
    DATA_MEGABYTES = 2
    DATA_GIGABYTES = 3
    DATA_TERABYTES = 4


def convert_unit(size: int, unit: Optional[str] = DATA_BYTES) -> int:
    """Convert the file size in bytes to kilobytes, megabytes, gigabytes, etc."""

    if unit == DATA_TERABYTES:
        size = round(size / (1024 ** Units.DATA_TERABYTES), 2)
    elif unit == DATA_GIGABYTES:
        size = round(size / (1024 ** Units.DATA_GIGABYTES), 2)
    elif unit == DATA_MEGABYTES:
        size = round(size / (1024 ** Units.DATA_MEGABYTES), 2)
    elif unit == DATA_KILOBYTES:
        size = round(size / (1024 ** Units.DATA_KILOBYTES), 2)
    elif unit == DATA_BYTES:
        size = round(size / (1024 ** Units.DATA_BYTES), 2)
    
    return size


def format_file_size(size: int) -> str:
    """Format file size from bytes to kilobytes, megabytes, gigabytes, etc."""

    if (size / (1024 ** Units.DATA_TERABYTES)) > 1:
        file_size = f"{str(convert_unit(size, DATA_TERABYTES))} {DATA_TERABYTES}"
    elif (size / (1024 ** Units.DATA_GIGABYTES)) > 1:
        file_size = f"{str(convert_unit(size, DATA_GIGABYTES))} {DATA_GIGABYTES}"
    elif (size / (1024 ** Units.DATA_MEGABYTES)) > 1:
        file_size = f"{str(convert_unit(size, DATA_MEGABYTES))} {DATA_MEGABYTES}"
    elif (size / (1024 ** Units.DATA_KILOBYTES)) > 1:
        file_size = f"{str(convert_unit(size, DATA_KILOBYTES))} {DATA_KILOBYTES}"
    else:
        file_size = f"{str(convert_unit(size, DATA_BYTES))} {DATA_BYTES}"

    return file_size


def format_timestamp(timestamp) -> str:
    """Format a timestamp."""

    time = datetime.fromtimestamp(timestamp)
    formatted_time = time.strftime('%Y-%m-%d %H:%M')

    return formatted_time


def get_files(root: str, user) -> List[Dict[str, str]]:
    """Return all files inside a directory."""

    files_ = []

    abspath = os.path.abspath(root)
    path, subdirs, files = next(os.walk(abspath))

    for name in files:
        last_modified_date = format_timestamp(os.path.getmtime(os.path.join(path, name)))
        size = os.path.getsize(os.path.join(path, name))
                
        files_.append({
            "path": os.path.join(path, name),
            "relative_path": os.path.relpath(os.path.join(path, name), user.storage_path),
            "name": name,
            "last_modified_date": last_modified_date,
            "size": format_file_size(size)
        })

    return files_


def get_subdirs(root: str, user) -> List[Dict[str, str]]:
    """Return all subdirectories inside a directory."""

    subdirs_ = []

    abspath = os.path.abspath(root)
    path, subdirs, files = next(os.walk(abspath))

    for subdir in subdirs:
        last_modified_date = format_timestamp(os.path.getmtime(os.path.join(path, subdir)))
        dir_size = os.path.getsize(os.path.join(path, subdir))
        
        subdirs_.append({
            "path": os.path.join(path, subdir),
            "relative_path": os.path.relpath(os.path.join(path, subdir), user.storage_path),
            "name": subdir,
            "listdir": [name for name in os.listdir(os.path.join(path, subdir))],
            "last_modified_date": last_modified_date
        })

    return subdirs_


def paths(root: str) -> List[str]:
    """List all paths that exist from the root path."""

    paths = []

    for path, subdirs, files in os.walk(root):
        paths.append(path)

    return paths


def paths_from_root_to_path(root: str, end: str) -> List[str]:
    """List all paths that exist from the root path up to a specific path."""

    paths = []
    
    for i in range(len(os.path.normcase(end).split(os.sep))):
        if os.path.normcase(root) in os.path.normcase(os.path.join(*(os.path.normcase(end).split(os.sep)[:i + 1]))):
            paths.append(os.path.join(*(os.path.normcase(end).split(os.sep)[:i + 1])))

    return paths