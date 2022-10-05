from src import config
from pathlib import Path
import tempfile
from werkzeug.utils import secure_filename
import os


def get_file_stem(file: str):
    return Path(file).stem


def get_file_ext(file: str):
    ext = file.split(".")[-1]
    return ext if "." in file and "/" not in ext else None


def get_file_from_path(file: str):
    ext = get_file_ext(file)
    stem = get_file_stem(file)
    return f"{stem}.{ext}" if ext is not None else stem


def is_file_allowed(file: str):
    return get_file_ext(file) in config.WHITELIST


def create_temp_dir():
    return tempfile.TemporaryDirectory()


def get_secure_filename(file: str):
    return secure_filename(file)


def join(paths: [str]):
    return os.path.join(*paths)
