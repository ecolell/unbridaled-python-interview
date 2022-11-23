from datetime import datetime
from typing import Dict, List, Optional

from app.models.product import ProductType, UOMType
from app.models.product_variant import ProductVariantType
from pydantic import BaseModel


class APIModel(BaseModel):
    class Config:
        json_encoders = {datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.%fZ")}


class ProductVariantCreate(APIModel):

    id: int
    sku: str
    sales_price: int
    product_id: int
    purchase_price: int
    type: ProductVariantType
    created_at: datetime
    updated_at: datetime
    config_attributes: List[Dict[str, str]]


class Product(APIModel):

    id: int
    name: str
    uom: UOMType
    category_name: str
    is_producible: bool
    is_purchasable: bool
    type: ProductType
    purchase_uom: Optional[UOMType]
    purchase_uom_conversion_rate: Optional[int]
    batch_tracked: bool
    additional_info: str
    created_at: datetime
    updated_at: datetime


class ProductCreate(Product):
    variants: List[ProductVariantCreate]
