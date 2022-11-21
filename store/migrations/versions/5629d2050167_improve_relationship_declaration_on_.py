"""improve relationship declaration on product and productvariant

Revision ID: 5629d2050167
Revises: d537939279ea
Create Date: 2022-11-21 06:37:07.139209

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '5629d2050167'
down_revision = 'd537939279ea'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'uom',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('product', 'type',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('product', 'purchase_uom',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('productvariant', 'type',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('productvariant', 'type',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('product', 'purchase_uom',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('product', 'type',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('product', 'uom',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###
