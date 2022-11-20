
from typing import Optional, List, TYPE_CHECKING
import enum

from sqlmodel import Field, SQLModel, Column, Enum, JSON, Relationship
from datetime import datetime
import sqlalchemy as sa

if TYPE_CHECKING:
    from .product import Product


class ProductVariantType(str, enum.Enum):
    product = "product"


class ProductVariant(SQLModel, table=True):
    
    class Config:
        arbitrary_types_allowed = True

    id: Optional[int] = Field(default=None, primary_key=True)
    sku: str
    sales_price: int
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    product: "Product" = Relationship()
    purchase_price: int
    type: ProductVariantType = Field(sa_column=Column(Enum(ProductVariantType)))
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)), nullable=False)
    updated_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)), nullable=False)
    config_attributes: List = Field(default=[], sa_column=Column(JSON))
