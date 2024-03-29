"""add user_notes optional colunm to main table

Revision ID: 16c0aed1417f
Revises: 718d7c931c45
Create Date: 2024-02-07 17:22:46.004419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16c0aed1417f'
down_revision: Union[str, None] = '718d7c931c45'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('weather', sa.Column('user_notes', sa.String(length=350), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('weather', 'user_notes')
    # ### end Alembic commands ###
