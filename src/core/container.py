import os

# from config.settings import APP_ENV
# from config.settings import OMP_NUM_THREADS
from src.chains.rag_chain import RAGChain
from src.embeddings.embedding_service import get_embedding_model
from src.services.chat_service import ChatService
from src.services.ingestion_service import IngestionService
from src.services.upload_service import UploadService
from src.utils.logger import logger
from src.vectordb.chroma_service import ChromaService


class ServiceContainer:

    def __init__(self):

        self._ready = False
        self._chroma_service = None
        self._ingestion_service = None
        self._upload_service = None
        self._chat_service = None

    def warmup(self) -> None:

        if self._ready:
            return

        # os.environ.setdefault("OMP_NUM_THREADS", OMP_NUM_THREADS)
        # os.environ.setdefault("MKL_NUM_THREADS", OMP_NUM_THREADS)

        # logger.info(
        #     "Starting service warmup (env=%s, threads=%s)...",
        #     APP_ENV,
        #     OMP_NUM_THREADS,
        # )

        get_embedding_model()

        chroma = self.get_chroma_service()

        if chroma.exists():
            chroma.load()
            logger.info("Existing vector database attached.")
        else:
            logger.info("No vector database yet. Upload a document to begin.")

        self.get_chat_service()

        self._ready = True
        logger.info("All services warmed up and ready.")

    @property
    def ready(self) -> bool:
        return self._ready

    def get_chroma_service(self) -> ChromaService:

        if self._chroma_service is None:
            self._chroma_service = ChromaService()

        return self._chroma_service

    def get_ingestion_service(self) -> IngestionService:

        if self._ingestion_service is None:
            self._ingestion_service = IngestionService(
                vector_db=self.get_chroma_service(),
            )

        return self._ingestion_service

    def get_upload_service(self) -> UploadService:

        if self._upload_service is None:
            self._upload_service = UploadService(
                ingestion_service=self.get_ingestion_service(),
            )

        return self._upload_service

    def get_chat_service(self) -> ChatService:

        if self._chat_service is None:
            self._chat_service = ChatService(
                vector_db=self.get_chroma_service(),
                rag_chain=RAGChain(),
            )

        return self._chat_service


container = ServiceContainer()
