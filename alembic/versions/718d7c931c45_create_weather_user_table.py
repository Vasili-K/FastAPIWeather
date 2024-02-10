"""create weather user table

Revision ID: 718d7c931c45
Revises: 9c13df585a8d
Create Date: 2024-02-06 08:38:21.873519

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '718d7c931c45'
down_revision: Union[str, None] = '9c13df585a8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'weather_user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('surname', sa.String(100), nullable=False),
        sa.Column('created_on', sa.DateTime()),
        sa.Column('updated_on', sa.DateTime())
    )


def downgrade() -> None:
    op.drop_table('weather_user')
