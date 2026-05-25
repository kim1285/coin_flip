from uuid import UUID

from fastapi import APIRouter
from starlette import status

from db import DBSessionDep
from src.api.coin.models import Coin
from src.api.coin.repository import create_coin as create_coin_repository
from src.api.coin.schemas import CreateCoinResponse

router = APIRouter(prefix="/coin", tags=["Coin"])


@router.post(
    "",
    response_model=CreateCoinResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Coin",
    description="Create Coin",
)
async def create_coin(session: DBSessionDep, user_id: UUID):
    coin = Coin(user_id=user_id)
    await create_coin_repository(session, coin)
    await session.commit()
    return CreateCoinResponse(coin_id=coin.id, created_at=coin.created_at)
