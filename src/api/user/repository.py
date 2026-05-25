from sqlalchemy.ext.asyncio import AsyncSession

from src.api.coin.models import User


async def create_user(session: AsyncSession, user: User):
    session.add(user)
    await session.flush()
    return user