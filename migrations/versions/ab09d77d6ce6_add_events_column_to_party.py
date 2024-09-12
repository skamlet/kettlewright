"""add events column to party

Revision ID: ab09d77d6ce6
Revises: c14144e7baef
Create Date: 2024-06-21 22:24:53.842854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab09d77d6ce6'
down_revision = 'c14144e7baef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parties', schema=None) as batch_op:
        batch_op.add_column(sa.Column('events', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parties', schema=None) as batch_op:
        batch_op.drop_column('events')

    # ### end Alembic commands ###