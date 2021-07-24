"""empty message

Revision ID: 60b3fdb3496e
Revises: 584805641171
Create Date: 2021-07-20 16:42:45.161064

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '60b3fdb3496e'
down_revision = '584805641171'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('provices',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('provices')
    # ### end Alembic commands ###