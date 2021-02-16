"""api v2

Revision ID: 3f4af6f2ac8a
Revises: f58fc2cc43f6
Create Date: 2021-02-15 23:22:28.311725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f4af6f2ac8a'
down_revision = 'f58fc2cc43f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('netid', sa.String(), nullable=True),
    sa.Column('upi', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('mailbox', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('preferred_name', sa.String(), nullable=True),
    sa.Column('middle_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('suffix', sa.String(), nullable=True),
    sa.Column('pronoun', sa.String(), nullable=True),
    sa.Column('school_code', sa.String(), nullable=True),
    sa.Column('school', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('curriculum', sa.String(), nullable=True),
    sa.Column('college', sa.String(), nullable=True),
    sa.Column('college_code', sa.String(), nullable=True),
    sa.Column('leave', sa.Boolean(), nullable=True),
    sa.Column('eli_whitney', sa.Boolean(), nullable=True),
    sa.Column('image_id', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('birthday', sa.String(), nullable=True),
    sa.Column('residence', sa.String(), nullable=True),
    sa.Column('building_code', sa.String(), nullable=True),
    sa.Column('entryway', sa.String(), nullable=True),
    sa.Column('floor', sa.Integer(), nullable=True),
    sa.Column('suite', sa.Integer(), nullable=True),
    sa.Column('room', sa.String(), nullable=True),
    sa.Column('major', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('access_code', sa.String(), nullable=True),
    sa.Column('organization_id', sa.String(), nullable=True),
    sa.Column('organization', sa.String(), nullable=True),
    sa.Column('unit_class', sa.String(), nullable=True),
    sa.Column('unit_code', sa.String(), nullable=True),
    sa.Column('unit', sa.String(), nullable=True),
    sa.Column('postal_address', sa.String(), nullable=True),
    sa.Column('office', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('key',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('uses', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('approved', sa.Boolean(), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.Integer(), nullable=True),
    sa.Column('last_used', sa.Integer(), nullable=True),
    sa.Column('user_username', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_username'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.drop_table('students')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('netid', sa.VARCHAR(), nullable=True),
    sa.Column('upi', sa.INTEGER(), nullable=True),
    sa.Column('first_name', sa.VARCHAR(), nullable=False),
    sa.Column('last_name', sa.VARCHAR(), nullable=False),
    sa.Column('image_id', sa.INTEGER(), nullable=True),
    sa.Column('image', sa.VARCHAR(), nullable=True),
    sa.Column('year', sa.INTEGER(), nullable=True),
    sa.Column('college', sa.VARCHAR(), nullable=True),
    sa.Column('pronoun', sa.VARCHAR(), nullable=True),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('residence', sa.VARCHAR(), nullable=True),
    sa.Column('building_code', sa.VARCHAR(), nullable=True),
    sa.Column('entryway', sa.VARCHAR(), nullable=True),
    sa.Column('floor', sa.INTEGER(), nullable=True),
    sa.Column('suite', sa.INTEGER(), nullable=True),
    sa.Column('room', sa.VARCHAR(), nullable=True),
    sa.Column('birthday', sa.VARCHAR(), nullable=True),
    sa.Column('major', sa.VARCHAR(), nullable=True),
    sa.Column('address', sa.VARCHAR(), nullable=True),
    sa.Column('phone', sa.VARCHAR(), nullable=True),
    sa.Column('leave', sa.BOOLEAN(), nullable=True),
    sa.Column('access_code', sa.VARCHAR(), nullable=True),
    sa.Column('eli_whitney', sa.BOOLEAN(), nullable=True),
    sa.CheckConstraint('leave IN (0, 1)'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('key')
    op.drop_table('person')
    # ### end Alembic commands ###