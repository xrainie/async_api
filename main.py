import uvicorn
from fastapi import FastAPI
from api_v1.product import router as product_router
from core.models.base import BaseModel
from core.db_helper import db_helper
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(product_router, prefix="/products")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
