from src.loaders.document_loader import DocumentLoader
from src.splitter.text_splitter import DocumentSplitter
from src.vectordb.chroma_service import ChromaService


class IngestionService:

    def __init__(self, vector_db: ChromaService):

        self.loader = DocumentLoader()
        self.splitter = DocumentSplitter()
        self.vector_db = vector_db

    def ingest_file(self, file_path: str) -> int:

        documents = self.loader.load_file(file_path)

        chunks = self.splitter.split_documents(documents)

        self.vector_db.add_documents(chunks)

        return len(chunks)

    def ingest(self):

        documents = self.loader.load_documents()

        chunks = self.splitter.split_documents(documents)

        self.vector_db.rebuild(chunks)
