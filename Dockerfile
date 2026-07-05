FROM python:3.12-slim
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_ENV=production \
    OMP_NUM_THREADS=1 \
    MKL_NUM_THREADS=1 \
    TOKENIZERS_PARALLELISM=false \
    HF_HOME=/app/.cache/huggingface \
    DOCUMENT_PATH=/app/docs \
    VECTOR_DB_PATH=/app/chroma_db

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./

RUN pip install --no-cache-dir uv \
    && uv sync --frozen --no-dev

COPY . .

RUN mkdir -p docs chroma_db .cache/huggingface \
    && uv run python -c "from src.embeddings.embedding_service import get_embedding_model; get_embedding_model()"

EXPOSE 8000

# Single worker only — each worker loads its own copy of the embedding model
CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
