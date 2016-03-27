"""empty message

Revision ID: 344e42afcf57
Revises: 24ccd86197ec
Create Date: 2016-03-26 17:52:44.626652

"""

# revision identifiers, used by Alembic.
revision = '344e42afcf57'
down_revision = '24ccd86197ec'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wishlist', 'description2')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wishlist', sa.Column('description2', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    ### end Alembic commands ###
