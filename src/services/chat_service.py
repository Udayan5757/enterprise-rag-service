from src.chains.rag_chain import RAGChain
from src.context.context_builder import ContextBuilder
from src.retrieval.retriever import RetrieverService
from src.vectordb.chroma_service import ChromaService


class ChatService:

    def __init__(self, vector_db: ChromaService, rag_chain: RAGChain):

        self.retriever = RetrieverService(vector_db)
        self.rag_chain = rag_chain

    def ask(self, question: str):

        documents = self.retriever.retrieve_documents(question)

        context, sources = ContextBuilder.build(documents)

        answer = self.rag_chain.invoke(
            context=context,
            question=question,
        )

        return {
            "answer": answer,
            "sources": sources,
        }
