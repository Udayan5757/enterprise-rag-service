from dotenv import load_dotenv
import os

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile",
)

CHAT_MODEL = os.getenv(
    "CHAT_MODEL",
    "gpt-4.1-mini",
)

DOCUMENT_PATH = os.getenv(
    "DOCUMENT_PATH",
    "docs",
)

VECTOR_DB_PATH = os.getenv(
    "VECTOR_DB_PATH",
    "chroma_db",
)

# local = HuggingFace on CPU (~400MB RAM) | openai = remote API (near-zero local RAM)
EMBEDDING_PROVIDER = os.getenv(
    "EMBEDDING_PROVIDER",
    "local",
).lower()

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2",
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Cache HuggingFace models on disk so they are not re-downloaded each restart
HF_HOME = os.getenv("HF_HOME", ".cache/huggingface")

# Limit CPU thread usage to reduce memory spikes on small servers
OMP_NUM_THREADS = os.getenv("OMP_NUM_THREADS", "1")

APP_ENV = os.getenv("APP_ENV", "development")
