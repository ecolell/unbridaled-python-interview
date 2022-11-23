from app.db import get_session
from app.services.product_service import ProductError, create_product
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from . import schemas

router = APIRouter(prefix="/products")


@router.post("/create", response_model=schemas.Product)
async def add_product(
    data: schemas.ProductCreate, session: AsyncSession = Depends(get_session)
) -> schemas.Product:
    try:
        product = await create_product(session, data)
    except ProductError:
        raise HTTPException(status_code=412, detail="Unable to create the product")
    return schemas.Product(**product.dict())
