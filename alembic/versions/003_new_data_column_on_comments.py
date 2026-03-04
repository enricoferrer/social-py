"""Create comments table

Revision ID: 003_new_data_column_on_comments
Revises: 002_create_comments_table
Create Date: 2026-03-04 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '003_new_data_column_on_comments'
down_revision: Union[str, None] = '002_create_comments_table'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = '002_create_comments_table'

def upgrade() -> None:
    # Create comments table
    op.add_column(
        'comments', sa.Column("commented_at", sa.DateTime)
    )


def downgrade() -> None:
    op.drop_column('comments', 'commented_at')