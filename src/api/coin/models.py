import uuid
from enum import StrEnum

from sqlalchemy import UUID, ForeignKey, String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from db import Base, TimeMixin


class CoinFlipResult(StrEnum):
    tail = "tail"
    head = "head"


class User(Base, TimeMixin):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class Coin(Base, TimeMixin):
    __tablename__ = "coins"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class CoinFlip(Base, TimeMixin):
    __tablename__ = "coin_flips"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    coin_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("coins.id", ondelete="CASCADE"))
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    result: Mapped[CoinFlipResult] = mapped_column(Enum(CoinFlipResult, values_callable=lambda x: [a.value for a in x]))
