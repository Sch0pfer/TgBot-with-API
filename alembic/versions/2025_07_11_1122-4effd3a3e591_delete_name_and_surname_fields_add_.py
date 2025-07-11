"""delete name and surname fields, add username field

Revision ID: 4effd3a3e591
Revises: b3859ab3170b
Create Date: 2025-07-11 11:22:58.641904

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4effd3a3e591"
down_revision: Union[str, Sequence[str], None] = "b3859ab3170b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("username", sa.String(), nullable=False))
    op.drop_column("users", "name")
    op.drop_column("users", "surname")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "surname", sa.VARCHAR(), autoincrement=False, nullable=False
        ),
    )
    op.add_column(
        "users",
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_column("users", "username")
    # ### end Alembic commands ###
