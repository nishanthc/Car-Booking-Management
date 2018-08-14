"""empty message

Revision ID: 7efed179ffd0
Revises: 
Create Date: 2018-08-13 21:45:30.859314

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '7efed179ffd0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('email_notifcations', sa.Boolean(), nullable=True),
    sa.Column('text_notifcations', sa.Boolean(), nullable=True),
    sa.Column('password', sqlalchemy_utils.types.password.PasswordType(), nullable=True),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
    sa.Column('mobile', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('level',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('email_notifcations', sa.Boolean(), nullable=True),
    sa.Column('text_notifcations', sa.Boolean(), nullable=True),
    sa.Column('date_enrolled', sa.DateTime(), nullable=True),
    sa.Column('password', sqlalchemy_utils.types.password.PasswordType(), nullable=True),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
    sa.Column('mobile', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('lesson',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('level_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('dateTime', sa.DateTime(), nullable=True),
    sa.Column('paid', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['level_id'], ['level.id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lesson')
    op.drop_table('user')
    op.drop_table('subject')
    op.drop_table('level')
    op.drop_table('admin')
    # ### end Alembic commands ###