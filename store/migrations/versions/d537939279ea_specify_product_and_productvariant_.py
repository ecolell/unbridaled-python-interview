"""specify product and productvariant tables

Revision ID: d537939279ea
Revises: 87ccd461cfc7
Create Date: 2022-11-21 02:20:27.369198

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
import sqlalchemy_utils
from app.models.product import ProductType, UOMType
from app.models.product_variant import ProductVariantType


# revision identifiers, used by Alembic.
revision = 'd537939279ea'
down_revision = '87ccd461cfc7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('uom', sqlalchemy_utils.types.choice.ChoiceType(UOMType), nullable=True),
    sa.Column('type', sqlalchemy_utils.types.choice.ChoiceType(ProductType), nullable=True),
    sa.Column('purchase_uom', sqlalchemy_utils.types.choice.ChoiceType(UOMType), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('category_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('is_producible', sa.Boolean(), nullable=False),
    sa.Column('is_purchasable', sa.Boolean(), nullable=False),
    sa.Column('purchase_uom_conversion_rate', sa.Integer(), nullable=False),
    sa.Column('additional_info', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('productvariant',
    sa.Column('type', sqlalchemy_utils.types.choice.ChoiceType(ProductVariantType), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('config_attributes', sa.JSON(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sku', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('sales_price', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('purchase_price', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productvariant')
    op.drop_table('product')
    # ### end Alembic commands ###
