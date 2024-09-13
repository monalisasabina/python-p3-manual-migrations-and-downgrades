"""renaming name to firstname

Revision ID: 40f5691b5622
Revises: c02f3aa85d4e
Create Date: 2024-09-13 21:06:16.477247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40f5691b5622'
down_revision = 'c02f3aa85d4e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # op.alter_column('my_table', 'old_col_name', nullable=False, new_column_name='new_col_name')
    op.alter_column('scholars','name',new_column_name='firstname')

def downgrade() -> None:
     op.alter_column('scholars','firstname',new_column_name='name')
