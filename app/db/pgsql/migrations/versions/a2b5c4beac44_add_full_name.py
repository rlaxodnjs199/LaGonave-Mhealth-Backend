"""Add full_name

Revision ID: a2b5c4beac44
Revises: 26af920c6095
Create Date: 2022-10-29 15:54:32.897831

"""
from alembic import op
from app.db.pgsql.session import engine
from app.db.pgsql.base import Base
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a2b5c4beac44"
down_revision = "26af920c6095"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
