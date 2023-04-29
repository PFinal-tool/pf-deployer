"""empty message

Revision ID: 42b3c099ddd8
Revises: d5ed9b98b466
Create Date: 2023-04-26 11:43:19.810564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42b3c099ddd8'
down_revision = 'd5ed9b98b466'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_admin_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('method', sa.String(length=10), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('ip', sa.String(length=255), nullable=True),
    sa.Column('success', sa.Integer(), nullable=True),
    sa.Column('user_agent', sa.Text(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin_admin_log')
    # ### end Alembic commands ###
