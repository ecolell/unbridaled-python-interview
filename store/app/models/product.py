from typing import Optional
import enum

import sqlalchemy as sa
import sqlalchemy_utils as sau
from sqlmodel import Field, SQLModel
from datetime import datetime


class ProductType(enum.Enum):
    product = "product"


class UOMType(enum.Enum):
    pcs = "pcs"


class ProductBase(SQLModel):
    name: str
    uom: UOMType = Field(sa_column=sa.Column(sau.ChoiceType(UOMType, impl=sa.String()), nullable=False))
    category_name: str
    is_producible: bool
    is_purchasable: bool
    type: ProductType = Field(sa_column=sa.Column(sau.ChoiceType(ProductType, impl=sa.String()), nullable=False))
    purchase_uom: UOMType = Field(sa_column=sa.Column(sau.ChoiceType(UOMType, impl=sa.String()), nullable=False))
    purchase_uom_conversion_rate: int
    additional_info: str
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)), nullable=False)
    updated_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)), nullable=False)


class Product(ProductBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class ProductCreate(ProductBase):
    pass