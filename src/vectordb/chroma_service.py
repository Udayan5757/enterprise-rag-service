import gc
import os
import shutil
import threading
import time

from langchain_chroma import Chroma

from config.settings import VECTOR_DB_PATH

from src.embeddings.embedding_service import get_embedding_model
from src.utils.logger import logger


class ChromaService:

    _db = None
    _lock = threading.Lock()

    def __init__(self):

        self.embedding_model = get_embedding_model()

    def _release(self):

        ChromaService._db = None
        gc.collect()

    def _safe_rmtree(self, path, retries=5, delay=0.5):

        for attempt in range(retries):

            try:

                if os.path.exists(path):
                    shutil.rmtree(path)

                return

            except PermissionError:

                if attempt == retries - 1:
                    raise

                logger.warning(
                    "Vector DB files locked, retrying delete (%s/%s)...",
                    attempt + 1,
                    retries,
                )

                self._release()
                time.sleep(delay)

    def exists(self):

        return os.path.exists(VECTOR_DB_PATH)

    def load(self):

        if ChromaService._db is not None:
            return ChromaService._db

        if not self.exists():
            raise FileNotFoundError(
                f"Vector database not found at {VECTOR_DB_PATH}"
            )

        logger.info("Loading Existing Vector Database...")

        ChromaService._db = Chroma(
            persist_directory=VECTOR_DB_PATH,
            embedding_function=self.embedding_model,
        )

        return ChromaService._db

    def create(self, chunks):

        logger.info("Creating Vector Database...")

        self._release()

        ChromaService._db = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory=VECTOR_DB_PATH,
        )

        logger.info("Vector Database Created Successfully.")

    def delete(self):

        if not self.exists():
            return

        logger.info("Deleting Existing Vector Database...")

        try:

            db = self.load()
            db._client.reset()

        except Exception as error:

            logger.warning(
                "Chroma reset failed (%s), falling back to file deletion.",
                error,
            )

            self._release()
            self._safe_rmtree(VECTOR_DB_PATH)

        finally:

            self._release()

        logger.info("Vector Database Deleted.")

    def add_documents(self, chunks):

        with ChromaService._lock:

            if self.exists():

                db = self.load()
                db.add_documents(chunks)

            else:

                self.create(chunks)

            logger.info("Indexed %s chunks.", len(chunks))

    def rebuild(self, chunks):

        with ChromaService._lock:

            logger.info("Rebuilding Vector Database...")

            self.delete()
            self.create(chunks)

            logger.info("Vector Database Rebuilt Successfully.")

    def similarity_search(self, query, k):

        with ChromaService._lock:

            db = self.load()

            return db.similarity_search(
                query=query,
                k=k,
            )
