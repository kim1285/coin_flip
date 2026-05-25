from fastapi import APIRouter
from starlette import status

from db import DBSessionDep
from src.api.coin.models import User
from src.api.user.schemas import CreateUserResponse, CreateUserRequest
from src.api.user.repository import create_user as create_user_repository
router = APIRouter(prefix="/user", tags=["User"])


@router.post(
    "",
    response_model=CreateUserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(create_user_request: CreateUserRequest, db_session: DBSessionDep) -> CreateUserResponse:
    user = User(username=create_user_request.username)
    await create_user_repository(db_session, user)
    await db_session.commit()
    await db_session.refresh(user)
    return CreateUserResponse(user_id=user.id, created_at=user.created_at)
