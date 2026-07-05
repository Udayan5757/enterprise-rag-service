#!/usr/bin/env bash
set -euo pipefail

export APP_ENV=production
export OMP_NUM_THREADS="${OMP_NUM_THREADS:-1}"
export MKL_NUM_THREADS="${MKL_NUM_THREADS:-1}"
export TOKENIZERS_PARALLELISM=false

# Never use --reload in production (loads the model twice and watches files)
exec uv run uvicorn app:app \
  --host 0.0.0.0 \
  --port "${PORT:-8000}" \
  --workers 1 \
  --timeout-keep-alive 120
