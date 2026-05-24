from fastapi import APIRouter
from starlette import status

from db import DBSessionDep
from src.api.coin.schemas import CreateCoinResponse

router = APIRouter(prefix="/coin", tags=["Coin"])


@router.post(
    "",
    response_model=CreateCoinResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Coin",
    description="Create Coin",
)
async def create_coin(session: DBSessionDep):
    # create coin
    pass
