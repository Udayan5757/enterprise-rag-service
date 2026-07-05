from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import UploadFile

from src.core.dependencies import get_upload_service
from src.services.upload_service import UploadService

router = APIRouter()


@router.post("/upload")
def upload(
    file: UploadFile = File(...),
    upload_service: UploadService = Depends(get_upload_service),
):

    return upload_service.upload(file)
