import enum
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

import sqlalchemy as sa
import sqlalchemy_utils as sau
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .product_variant import ProductVariant


class ProductType(enum.Enum):
    product = "product"


class UOMType(enum.Enum):
    pcs = "pcs"
    kg = "kg"
    m = "m"


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=sa.Column("name", sa.Text, unique=True))
    uom: UOMType = Field(
        sa_column=sa.Column(sau.ChoiceType(UOMType, impl=sa.String()), nullable=False)
    )
    category_name: str
    is_producible: bool
    is_purchasable: bool
    type: ProductType = Field(
        sa_column=sa.Column(
            sau.ChoiceType(ProductType, impl=sa.String()), nullable=False
        )
    )
    purchase_uom: UOMType = Field(
        sa_column=sa.Column(sau.ChoiceType(UOMType, impl=sa.String()), nullable=False)
    )
    purchase_uom_conversion_rate: int
    additional_info: str
    created_at: datetime = Field(
        sa_column=sa.Column(sa.DateTime(timezone=True)), nullable=False
    )
    updated_at: datetime = Field(
        sa_column=sa.Column(sa.DateTime(timezone=True)), nullable=False
    )
    variants: List["ProductVariant"] = Relationship(back_populates="product")
