"""empty message

Revision ID: 68f003ba83e1
Revises: 8b348cb5fa6c
Create Date: 2022-09-03 01:57:41.034580

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '68f003ba83e1'
down_revision = '8b348cb5fa6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('favorito', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('mass', sa.Integer(), nullable=False),
    sa.Column('hair_color', sa.String(length=250), nullable=False),
    sa.Column('eye_color', sa.String(length=250), nullable=False),
    sa.Column('gender', sa.String(length=30), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'user_id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=False),
    sa.Column('orbital_period', sa.Integer(), nullable=False),
    sa.Column('gravity', sa.Integer(), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('terrain', sa.String(length=250), nullable=False),
    sa.Column('surface_water', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'user_id')
    )
    op.create_table('starships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('model', sa.String(length=250), nullable=False),
    sa.Column('length', sa.Integer(), nullable=False),
    sa.Column('crew', sa.Integer(), nullable=False),
    sa.Column('passengers', sa.Integer(), nullable=False),
    sa.Column('manufacturer', sa.String(length=250), nullable=False),
    sa.Column('max_atmosphering_speed', sa.Integer(), nullable=False),
    sa.Column('cargo_capacity', sa.Integer(), nullable=False),
    sa.Column('consumables', sa.String(length=250), nullable=False),
    sa.Column('cost_in_credits', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('name', sa.String(length=250), nullable=False))
    op.add_column('user', sa.Column('nickname', sa.String(length=250), nullable=False))
    op.drop_index('email', table_name='user')
    op.drop_index('email_2', table_name='user')
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.create_index('email_2', 'user', ['email'], unique=False)
    op.create_index('email', 'user', ['email'], unique=False)
    op.drop_column('user', 'nickname')
    op.drop_column('user', 'name')
    op.drop_table('starships')
    op.drop_table('planets')
    op.drop_table('character')
    op.drop_table('favorite')
    # ### end Alembic commands ###
