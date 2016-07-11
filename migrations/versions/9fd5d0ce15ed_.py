"""empty message

Revision ID: 9fd5d0ce15ed
Revises: 317d449569f6
Create Date: 2016-05-03 10:45:37.138782

"""

# revision identifiers, used by Alembic.
revision = '9fd5d0ce15ed'
down_revision = '317d449569f6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
