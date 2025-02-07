"""4_rename address

Revision ID: 8268ca1eb455
Revises: 7709d8b3f82e
Create Date: 2024-10-23 01:29:10.920334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8268ca1eb455'
down_revision = '7709d8b3f82e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
