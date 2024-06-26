"""user, book_copy, sharing tables added

Revision ID: 55c7650e0a43
Revises: 
Create Date: 2024-03-23 18:53:57.035161

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '55c7650e0a43'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookread')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookread',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], name='bookread_author_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='bookread_pkey')
    )
    # ### end Alembic commands ###
