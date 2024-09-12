"""add gold, description, and notes

Revision ID: eeb57e7c4b39
Revises: cd5bb0fc8a17
Create Date: 2023-11-18 11:22:00.743240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eeb57e7c4b39'
down_revision = 'cd5bb0fc8a17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gold', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('description', sa.String(length=2000), nullable=True))
        batch_op.add_column(sa.Column('notes', sa.String(length=2000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.drop_column('notes')
        batch_op.drop_column('description')
        batch_op.drop_column('gold')

    # ### end Alembic commands ###