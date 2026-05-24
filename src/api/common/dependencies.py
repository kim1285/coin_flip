from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI


def get_lifespan():
    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        # connect to db, start db session pool
        yield
        # clean up db session pool and any connections
    return lifespan
