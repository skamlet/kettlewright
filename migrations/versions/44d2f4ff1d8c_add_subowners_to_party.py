"""add subowners to party

Revision ID: 44d2f4ff1d8c
Revises: 00d5f6f873e2
Create Date: 2024-07-13 13:31:35.814939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44d2f4ff1d8c'
down_revision = '00d5f6f873e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parties', schema=None) as batch_op:
        batch_op.add_column(sa.Column('subowners', sa.String(length=2000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parties', schema=None) as batch_op:
        batch_op.drop_column('subowners')

    # ### end Alembic commands ###