"""create npm log schema

Revision ID: f089c907d437
Revises: 4cb84c335871
Create Date: 2022-11-30 21:13:52.292588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f089c907d437'
down_revision = '4cb84c335871'
branch_labels = None
depends_on = None
schema_name = 'npm_log'


def upgrade():
    op.execute(f"CREATE SCHEMA {schema_name}")


def downgrade():
    op.execute(f"DROP SCHEMA {schema_name}")
