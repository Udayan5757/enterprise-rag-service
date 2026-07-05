from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader

from config.constants import SUPPORTED_EXTENSIONS
from config.settings import DOCUMENT_PATH

from src.utils.logger import logger


class DocumentLoader:

    def load_file(self, file_path: str):

        path = Path(file_path)
        extension = path.suffix.lower()

        if extension not in SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type '{extension}'. "
                f"Supported: {', '.join(sorted(SUPPORTED_EXTENSIONS))}"
            )

        logger.info("Loading document: %s", path.name)

        if extension == ".pdf":
            loader = PyPDFLoader(str(path))
        else:
            loader = TextLoader(str(path))

        documents = loader.load()

        logger.info("%s pages/sections loaded from %s.", len(documents), path.name)

        return documents

    def load_documents(self):

        try:

            logger.info("Loading documents...")

            documents = []

            text_loader = DirectoryLoader(
                path=DOCUMENT_PATH,
                glob="**/*.txt",
                loader_cls=TextLoader
            )

            pdf_loader = DirectoryLoader(
                path=DOCUMENT_PATH,
                glob="**/*.pdf",
                loader_cls=PyPDFLoader
            )

            documents.extend(text_loader.load())

            documents.extend(pdf_loader.load())

            logger.info(f"{len(documents)} documents loaded successfully.")

            return documents

        except Exception as e:

            logger.error(e)

            raise