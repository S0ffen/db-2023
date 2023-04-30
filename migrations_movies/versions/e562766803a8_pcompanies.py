"""

pcompanies

Revision ID: e562766803a8
Creation date: 2023-04-30 22:38:06.579258

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'e562766803a8'
down_revision = '03a94830a8ac'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE TABLE pcompanies(
    company_id serial NOT NULL unique PRIMARY KEY,
    name TEXT NOT NULL
    );
    """)


def downgrade() -> None:
    op.execute("""
    DROP TABLE IF EXISTS pcompanies CASCADE;
    """)
