"""empty message

Revision ID: b1d675863ba3
Revises: None
Create Date: 2016-05-25 12:43:59.094649

"""

# revision identifiers, used by Alembic.
revision = 'b1d675863ba3'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'employees',
        sa.Column('full_name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('phone_number', sa.String(), nullable=False),
        sa.Column('image_url', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('email'),
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    ### end Alembic commands ###
