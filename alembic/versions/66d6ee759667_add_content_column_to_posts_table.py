"""add content column to posts table

Revision ID: 66d6ee759667
Revises: a6e71b3cf37b
Create Date: 2022-02-03 22:42:10.077781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66d6ee759667'
down_revision = 'a6e71b3cf37b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
