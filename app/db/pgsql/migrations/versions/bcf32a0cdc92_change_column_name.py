"""Change Column name

Revision ID: bcf32a0cdc92
Revises: c7a5ec80a2ea
Create Date: 2022-10-29 22:30:22.451183

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bcf32a0cdc92'
down_revision = 'c7a5ec80a2ea'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('lg_patient', 'recorder_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('lg_patient', 'recorder_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    # ### end Alembic commands ###