"""relationship updated

Revision ID: c3cc1da574ab
Revises: 7c1d011842dd
Create Date: 2025-01-14 12:37:04.146951

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c3cc1da574ab'
down_revision = '7c1d011842dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('addresses', schema=None) as batch_op:
        batch_op.drop_constraint('addresses_created_by_fkey', type_='foreignkey')
        batch_op.drop_constraint('addresses_updated_by_fkey', type_='foreignkey')
        batch_op.drop_constraint('addresses_business_id_fkey', type_='foreignkey')
        batch_op.drop_column('created_by')
        batch_op.drop_column('updated_by')
        batch_op.drop_column('business_id')
        batch_op.drop_column('created_at')
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('addresses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('business_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('updated_by', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('created_by', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('addresses_business_id_fkey', 'businesses', ['business_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('addresses_updated_by_fkey', 'users', ['updated_by'], ['id'], ondelete='SET NULL')
        batch_op.create_foreign_key('addresses_created_by_fkey', 'users', ['created_by'], ['id'], ondelete='SET NULL')

    # ### end Alembic commands ###
