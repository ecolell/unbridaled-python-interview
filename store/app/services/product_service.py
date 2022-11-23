from typing import TYPE_CHECKING

import sqlalchemy as sa
from app.models.product import Product
from app.models.product_variant import ProductVariant
from sqlalchemy.ext.asyncio import AsyncSession

if TYPE_CHECKING:
    from app.routers.v1.schemas import ProductCreate


class ProductError(Exception):
    pass


async def create_product(session: AsyncSession, data: "ProductCreate") -> "Product":
    product_data = data.dict(exclude={"variants"})
    product = Product(**product_data)
    session.add(product)
    variants = []
    for data_variant in data.variants:
        product_variant_data = data_variant.dict()
        variant = ProductVariant(**product_variant_data)
        variants.append(variant)
        session.add(variant)
    product.variants = variants
    try:
        await session.commit()
        await session.refresh(product)
    except sa.exc.IntegrityError:
        await session.rollback()
        raise ProductError()
    return product
