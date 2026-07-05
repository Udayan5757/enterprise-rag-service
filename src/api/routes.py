from fastapi import APIRouter
from fastapi import Depends

from config.settings import APP_ENV
from src.core.container import container
from src.core.dependencies import get_chat_service
from src.models.request import ChatRequest
from src.models.response import ChatResponse
from src.services.chat_service import ChatService

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service),
):

    result = chat_service.ask(request.question)

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"],
    )


@router.get("/health")
def health():

    return {
        "status": "UP" if container.ready else "STARTING",
        "env": APP_ENV,
        "services_ready": container.ready,
    }
