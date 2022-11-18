"""create demo test schema

Revision ID: 4cb84c335871
Revises: 
Create Date: 2022-11-17 16:11:18.233609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cb84c335871'
down_revision = None
branch_labels = None
depends_on = None
schema_name = 'test_schema'


def upgrade():
    op.execute(f"CREATE SCHEMA {schema_name}")


def downgrade():
    op.execute(f"DROP SCHEMA {schema_name}")
