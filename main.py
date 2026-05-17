from fastapi import FastAPI
from src.api.coin.routers import router as coin_router
from src.api.common.dependencies import get_lifecycle

app = FastAPI(lifespan=get_lifecycle())


app.include_router(coin_router)

