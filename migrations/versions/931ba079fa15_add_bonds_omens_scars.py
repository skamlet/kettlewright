"""add bonds, omens, scars

Revision ID: 931ba079fa15
Revises: eeb57e7c4b39
Create Date: 2023-11-25 12:41:15.373860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '931ba079fa15'
down_revision = 'eeb57e7c4b39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bonds', sa.String(length=2000), nullable=True))
        batch_op.add_column(sa.Column('scars', sa.String(length=2000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.drop_column('scars')
        batch_op.drop_column('bonds')

    # ### end Alembic commands ###