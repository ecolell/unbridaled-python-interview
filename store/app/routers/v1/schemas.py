from datetime import datetime
from typing import List

from app.models.product import ProductType, UOMType
from pydantic import BaseModel


class ProductVariantCreate(BaseModel):
    pass


class ProductCreate(BaseModel):
    name: str
    uom: UOMType
    category_name: str
    is_producible: bool
    is_purchasable: bool
    type: ProductType
    purchase_uom: UOMType
    purchase_uom_conversion_rate: int
    additional_info: str
    created_at: datetime
    updated_at: datetime
    variants: List[ProductVariantCreate]
