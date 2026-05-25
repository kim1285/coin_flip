from sqlalchemy.ext.asyncio import AsyncSession

from src.api.coin.models import Coin


async def create_coin(session: AsyncSession, coin: Coin):
    session.add(coin)
    await session.flush()
    return coin
