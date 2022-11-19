from typing import Optional
import enum

from sqlmodel import Field, SQLModel, Column, Enum
from datetime import datetime


class ProductType(str, enum.Enum):
    product = "product"


class UOMType(str, enum.Enum):
    pcs = "pcs"


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    uom: UOMType = Field(sa_column=Column(Enum(UOMType)))
    category_name: str
    is_producible: bool
    is_purchasable: bool
    type: ProductType = Field(sa_column=Column(Enum(ProductType)))
    purchase_uom: UOMType = Field(sa_column=Column(Enum(UOMType)))
    purchase_uom_conversion_rate: int
    additional_info: str
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
