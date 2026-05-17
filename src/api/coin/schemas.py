import uuid

from pydantic import BaseModel, AwareDatetime


class CreateCoinResponse(BaseModel):
    coin_id: uuid.UUID
    create_at: AwareDatetime
