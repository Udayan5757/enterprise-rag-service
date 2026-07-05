from config.constants import TOP_K_RESULTS

from src.vectordb.chroma_service import ChromaService


class RetrieverService:

    def __init__(self, vector_db: ChromaService):

        self.vector_store = vector_db

    def retrieve_documents(self, query):

        return self.vector_store.similarity_search(
            query=query,
            k=TOP_K_RESULTS,
        )
