from app.db import get_session
from app.models.product import Product, ProductCreate
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/products")


@router.post("/create")
async def add_product(data: ProductCreate, session: AsyncSession=Depends(get_session)):
    product = Product(**data.__dict__)
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product
