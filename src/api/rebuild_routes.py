from fastapi import APIRouter
from fastapi import Depends

from src.core.dependencies import get_ingestion_service
from src.services.ingestion_service import IngestionService

router = APIRouter()


@router.post("/rebuild")
def rebuild(
    ingestion_service: IngestionService = Depends(get_ingestion_service),
):

    ingestion_service.ingest()

    return {
        "message": "Knowledge Base Rebuilt Successfully",
    }
