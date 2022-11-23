from app.db import get_session
from app.models.product import Product
from app.services.products import create_product
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import schemas

router = APIRouter(prefix="/products")


@router.post("/create")
async def add_product(
    data: schemas.ProductCreate, session: AsyncSession = Depends(get_session)
):
    product = create_product(session, data)
    return product
