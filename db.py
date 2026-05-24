from functools import lru_cache
from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, AsyncEngine

from config import SettingsDep


@lru_cache
def get_engine(db_url) -> AsyncEngine:
    engine = create_async_engine(url=db_url, echo=True)
    return engine


@lru_cache
def get_async_session_maker(settings: SettingsDep) -> async_sessionmaker[AsyncSession]:
    engine = get_engine(settings.db_url)
    return async_sessionmaker(engine)


DBSessionMakerDep = Annotated[async_sessionmaker[AsyncSession], Depends(get_async_session_maker)]


async def get_session(async_session_maker: DBSessionMakerDep) -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


DBSessionDep = Annotated[AsyncSession, Depends(get_session)]
