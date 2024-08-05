from fastapi import APIRouter, HTTPException, status, Depends
from .schemas import Product, ProductCreate
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from core.db_helper import get_db

from typing import Annotated

router = APIRouter(tags=["products"])


@router.get("/", response_model=list[Product])
async def get_products(session: Annotated[AsyncSession, Depends(get_db)]):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(
    session: Annotated[AsyncSession, Depends(get_db)], product_in: ProductCreate
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}/", response_model=Product)
async def get_product(
    session: Annotated[AsyncSession, Depends(get_db)], product_id: int
):
    product = await crud.get_product(session=session, product_id=product_id)
    if product is not None:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Товара с данным id не существует.",
    )
