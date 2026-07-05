from contextlib import asynccontextmanager

from fastapi import FastAPI

from config.settings import APP_ENV
from src.api.routes import router
from src.api.upload_routes import router as upload_router
from src.core.container import container
from src.utils.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("Application startup (env=%s)", APP_ENV)
    container.warmup()
    app.state.container = container

    yield

    logger.info("Application shutdown")


app = FastAPI(
    title="Enterprise AI Knowledge Assistant",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(router)
app.include_router(upload_router)
