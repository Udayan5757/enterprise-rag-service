import threading

from langchain_groq import ChatGroq

from config.settings import GROQ_API_KEY
from config.settings import GROQ_MODEL
from src.utils.logger import logger

_llm = None
_lock = threading.Lock()


def get_llm():

    global _llm

    if _llm is not None:
        return _llm

    with _lock:

        if _llm is None:

            logger.info("Initializing Groq LLM: %s", GROQ_MODEL)

            _llm = ChatGroq(
                api_key=GROQ_API_KEY,
                model=GROQ_MODEL,
                temperature=0,
            )

    return _llm
