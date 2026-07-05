import os
import threading

from config.settings import EMBEDDING_MODEL
from config.settings import EMBEDDING_PROVIDER
from config.settings import HF_HOME
from config.settings import OPENAI_API_KEY
from src.utils.logger import logger

_embedding_model = None
_lock = threading.Lock()


def _configure_cache() -> None:

    os.makedirs(HF_HOME, exist_ok=True)
    os.environ.setdefault("HF_HOME", HF_HOME)
    os.environ.setdefault("TRANSFORMERS_CACHE", HF_HOME)
    os.environ.setdefault("SENTENCE_TRANSFORMERS_HOME", HF_HOME)
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")


def _build_local_embeddings():

    from langchain_huggingface import HuggingFaceEmbeddings

    logger.info("Loading local embedding model: %s", EMBEDDING_MODEL)

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )


def _build_openai_embeddings():

    from langchain_openai import OpenAIEmbeddings

    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY is required when EMBEDDING_PROVIDER=openai"
        )

    logger.info("Using OpenAI embeddings (no local model loaded).")

    return OpenAIEmbeddings(
        model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"),
        api_key=OPENAI_API_KEY,
    )


def _create_embedding_model():

    _configure_cache()

    if EMBEDDING_PROVIDER == "openai":
        return _build_openai_embeddings()

    if EMBEDDING_PROVIDER == "local":
        return _build_local_embeddings()

    raise ValueError(
        f"Unsupported EMBEDDING_PROVIDER '{EMBEDDING_PROVIDER}'. "
        "Use 'local' or 'openai'."
    )


def get_embedding_model():

    global _embedding_model

    if _embedding_model is not None:
        return _embedding_model

    with _lock:

        if _embedding_model is None:
            _embedding_model = _create_embedding_model()
            logger.info("Embedding model loaded and cached in memory.")

    return _embedding_model
