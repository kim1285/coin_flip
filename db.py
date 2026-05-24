from datetime import timezone, datetime
from functools import lru_cache
from typing import Annotated, AsyncGenerator

from fastapi import Depends
from pydantic import AwareDatetime
from sqlalchemy import func, DateTime
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, AsyncEngine, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

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


class Base(AsyncAttrs, DeclarativeBase):
    pass


def utcnow() -> AwareDatetime:
    return datetime.now(timezone.utc)


class CreatedAtMixin:
    created_at: Mapped[AwareDatetime] = mapped_column(
        DateTime(timezone=True),
        default=utcnow,
        server_default=func.now(),
        nullable=False,
    )


class UpdatedAtMixin:
    updated_at: Mapped[AwareDatetime] = mapped_column(
        DateTime(timezone=True),
        default=utcnow,
        server_default=func.now(),
        nullable=False,
    )


class TimeMixin(CreatedAtMixin, UpdatedAtMixin):
    pass
