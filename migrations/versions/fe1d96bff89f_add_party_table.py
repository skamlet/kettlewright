"""add party table

Revision ID: fe1d96bff89f
Revises: 443ca2ccd85b
Create Date: 2024-02-19 09:47:24.701557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe1d96bff89f'
down_revision = '443ca2ccd85b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=2000), nullable=True),
    sa.Column('notes', sa.String(length=2000), nullable=True),
    sa.Column('members', sa.String(length=2000), nullable=True),
    sa.Column('join_code', sa.String(length=64), nullable=True),
    sa.Column('party_url', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parties')
    # ### end Alembic commands ###