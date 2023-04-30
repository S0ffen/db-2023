"""

movie companies

Revision ID: d03523ba76c4
Creation date: 2023-04-30 23:23:27.982678

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'd03523ba76c4'
down_revision = 'e562766803a8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    CREATE TABLE movie_companies(
    movie_id int references movies(movie_id) on delete cascade,
    company_id int references pcompanies(company_id) on delete cascade
    );
    """)


def downgrade() -> None:
    op.execute("""
    DROP TABLE IF EXISTS movie_companies CASCADE;
    """)