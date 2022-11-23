from typing import TYPE_CHECKING
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product

if TYPE_CHECKING:
    from app.routers.v1 import ProductCreate


class ProductError(Exception):
    pass


async def create_product(session: AsyncSession, data: "ProductCreate") -> "Product":
    product = Product(**data.__dict__)
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product
