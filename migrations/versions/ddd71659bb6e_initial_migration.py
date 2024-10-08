"""Initial migration.

Revision ID: ddd71659bb6e
Revises: 
Create Date: 2024-08-10 18:10:26.089549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddd71659bb6e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.add_column(sa.Column('isAdmin', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('isPowerUser', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('isApprover', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.drop_column('isApprover')
        batch_op.drop_column('isPowerUser')
        batch_op.drop_column('isAdmin')

    # ### end Alembic commands ###
