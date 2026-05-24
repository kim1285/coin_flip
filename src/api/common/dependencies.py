from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from config import get_settings
from db import get_engine


def get_lifespan():
    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        settings = get_settings()
        # connect to db, start db session pool
        engine = get_engine(settings.db_url)
        yield
        await engine.dispose()
        # clean up db session pool and any connections
    return lifespan
