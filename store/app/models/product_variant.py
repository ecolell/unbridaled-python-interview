import enum
from datetime import datetime
from typing import TYPE_CHECKING, Dict, List, Optional

import sqlalchemy as sa
import sqlalchemy_utils as sau
from sqlmodel import JSON, Column, Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .product import Product


class ProductVariantType(enum.Enum):
    product = "product"


class ProductVariant(SQLModel, table=True):  # nomypy
    class Config:
        arbitrary_types_allowed = True

    id: Optional[int] = Field(default=None, primary_key=True)
    sku: str
    sales_price: int
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    product: Optional["Product"] = Relationship(back_populates="variants")
    purchase_price: int
    type: ProductVariantType = Field(
        sa_column=sa.Column(
            sau.ChoiceType(ProductVariantType, impl=sa.String()), nullable=False
        )
    )
    created_at: datetime = Field(
        sa_column=sa.Column(sa.DateTime(timezone=True)), nullable=False
    )
    updated_at: datetime = Field(
        sa_column=sa.Column(sa.DateTime(timezone=True)), nullable=False
    )
    config_attributes: List[Dict[str, str]] = Field(default=[], sa_column=Column(JSON))
