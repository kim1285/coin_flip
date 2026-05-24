from fastapi import FastAPI

from src.api.coin.routers import router as coin_router
from src.api.common.dependencies import get_lifespan

app = FastAPI(lifespan=get_lifespan())

app.include_router(coin_router)


@app.get("/ping")
async def ping():
    return {"message": "pong"}
