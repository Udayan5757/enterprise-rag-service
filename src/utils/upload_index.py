import json
from pathlib import Path

from config.constants import UPLOAD_INDEX_FILE
from config.settings import DOCUMENT_PATH


def _index_path() -> Path:

    return Path(DOCUMENT_PATH) / UPLOAD_INDEX_FILE


def load_index() -> dict[str, str]:

    path = _index_path()

    if not path.exists():
        return {}

    with open(path, encoding="utf-8") as file:
        return json.load(file)


def save_index(index: dict[str, str]) -> None:

    path = _index_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(index, file, indent=2)


def find_duplicate(filename: str, content_hash: str) -> str | None:

    destination = Path(DOCUMENT_PATH) / filename

    if destination.exists():
        return f"'{filename}' is already uploaded."

    index = load_index()

    for existing_name, existing_hash in index.items():

        if existing_hash == content_hash:
            return (
                f"This document is already uploaded as '{existing_name}'."
            )

    return None


def register_upload(filename: str, content_hash: str) -> None:

    index = load_index()
    index[filename] = content_hash
    save_index(index)
