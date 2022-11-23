from app.db import get_session
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from store.app.services.product_service import create_product

from . import schemas

router = APIRouter(prefix="/products")


@router.post("/create")
async def add_product(
    data: schemas.ProductCreate, session: AsyncSession = Depends(get_session)
):
    product = create_product(session, data)
    return product
