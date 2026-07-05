from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.constants import CHUNK_OVERLAP
from config.constants import CHUNK_SIZE

from src.utils.logger import logger


class DocumentSplitter:

    def __init__(self):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

    def split_documents(self, documents):

        logger.info("Splitting documents into chunks...")

        chunks = self.text_splitter.split_documents(documents)

        logger.info(f"{len(chunks)} chunks created.")

        return chunks