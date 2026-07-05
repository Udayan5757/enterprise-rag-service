import hashlib
from pathlib import Path

from config.constants import SUPPORTED_EXTENSIONS
from config.settings import DOCUMENT_PATH

from src.services.ingestion_service import IngestionService
from src.utils.upload_index import find_duplicate
from src.utils.upload_index import register_upload


class UploadService:

    def __init__(self, ingestion_service: IngestionService):

        self.ingestion_service = ingestion_service

    def upload(self, file):

        filename = Path(file.filename).name
        extension = Path(filename).suffix.lower()

        if extension not in SUPPORTED_EXTENSIONS:
            return {
                "duplicate": False,
                "indexed": False,
                "filename": filename,
                "message": (
                    f"Unsupported file type '{extension}'. "
                    f"Supported: {', '.join(sorted(SUPPORTED_EXTENSIONS))}"
                ),
            }

        content = file.file.read()
        content_hash = hashlib.sha256(content).hexdigest()

        duplicate_reason = find_duplicate(filename, content_hash)

        if duplicate_reason:
            return {
                "duplicate": True,
                "indexed": False,
                "filename": filename,
                "message": duplicate_reason,
            }

        destination = Path(DOCUMENT_PATH) / filename
        destination.parent.mkdir(parents=True, exist_ok=True)

        try:

            with open(destination, "wb") as buffer:
                buffer.write(content)

            chunks = self.ingestion_service.ingest_file(str(destination))

            register_upload(filename, content_hash)

            return {
                "duplicate": False,
                "indexed": True,
                "filename": filename,
                "chunks": chunks,
                "message": (
                    f"'{filename}' uploaded and indexed. "
                    "You can ask questions now."
                ),
            }

        except Exception:

            if destination.exists():
                destination.unlink()

            raise
