"""Renaming students to scholars

Revision ID: c02f3aa85d4e
Revises: 791279dd0760
Create Date: 2024-09-13 19:01:43.824387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c02f3aa85d4e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')


