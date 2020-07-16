"""empty message

Revision ID: 234afb72673
Revises: 157738e54a8
Create Date: 2020-07-09 20:55:44.851550

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '234afb72673'
down_revision = '157738e54a8'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('scheme', schema=None) as batch_op:
        batch_op.add_column(sa.Column('approved_districts', sa.String(length=126), nullable=True))
        batch_op.add_column(sa.Column('approved_states', sa.String(length=52), nullable=False))
        batch_op.add_column(sa.Column('benefits', sa.String(length=512), nullable=True))
        batch_op.add_column(sa.Column('creator', sa.String(length=52), nullable=False))
        batch_op.add_column(sa.Column('description', sa.String(length=512), nullable=True))
        batch_op.add_column(sa.Column('eligibility', sa.String(length=256), nullable=True))
        batch_op.add_column(sa.Column('feature', sa.String(length=512), nullable=True))
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('name', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('objective', sa.String(length=512), nullable=True))
        batch_op.drop_column('scheme_id')
        batch_op.drop_column('scheme_name')

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('scheme', schema=None) as batch_op:
        batch_op.add_column(sa.Column('scheme_name', sa.VARCHAR(length=50), nullable=False))
        batch_op.add_column(sa.Column('scheme_id', sa.INTEGER(), nullable=False))
        batch_op.drop_column('objective')
        batch_op.drop_column('name')
        batch_op.drop_column('id')
        batch_op.drop_column('feature')
        batch_op.drop_column('eligibility')
        batch_op.drop_column('description')
        batch_op.drop_column('creator')
        batch_op.drop_column('benefits')
        batch_op.drop_column('approved_states')
        batch_op.drop_column('approved_districts')

    ### end Alembic commands ###
