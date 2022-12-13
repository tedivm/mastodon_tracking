"""software version breakdowns

Revision ID: b69dbaa8f2d8
Revises: f4f9ee0f606b
Create Date: 2022-12-12 23:08:42.961928

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b69dbaa8f2d8"
down_revision = "f4f9ee0f606b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("instances", sa.Column("software", sa.String(), nullable=True))
    op.add_column("instances", sa.Column("mastodon_version", sa.String(), nullable=True))
    op.add_column("instances", sa.Column("software_version", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("instances", "software_version")
    op.drop_column("instances", "mastodon_version")
    op.drop_column("instances", "software")
    # ### end Alembic commands ###
