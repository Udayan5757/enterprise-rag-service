from src.core.container import container
from src.services.chat_service import ChatService
from src.services.ingestion_service import IngestionService
from src.services.upload_service import UploadService


def get_upload_service() -> UploadService:
    return container.get_upload_service()


def get_chat_service() -> ChatService:
    return container.get_chat_service()


def get_ingestion_service() -> IngestionService:
    return container.get_ingestion_service()
