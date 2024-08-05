from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from core.models.product import ProductModel
from .schemas import Product, ProductCreate


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(ProductModel).order_by(ProductModel.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(ProductModel, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = ProductModel(**product_in.model_dump())
    session.add(product)
    await session.commit()
    return product
