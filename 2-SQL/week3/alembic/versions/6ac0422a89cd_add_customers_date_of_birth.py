"""add customers date_of_birth

Revision ID: 6ac0422a89cd
Revises: 42e160df45e8
Create Date: 2022-08-24 19:17:13.980567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ac0422a89cd'
down_revision = '42e160df45e8'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )
