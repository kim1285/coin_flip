from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, AwareDatetime, Field


class CreateUserResponse(BaseModel):
    user_id: UUID
    created_at: AwareDatetime

class CreateUserRequest(BaseModel):
    username: UserName


UserName = Annotated[str, Field(description="name of a user.", examples=["Ford Prefect, Marvin,"])]
