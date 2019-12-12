"""empty message

Revision ID: bf17dcc74a5c
Revises: 1f1df7ffd629
Create Date: 2019-12-10 00:45:34.619251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf17dcc74a5c'
down_revision = '1f1df7ffd629'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'booking', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'booking', 'machines', ['machine_id'], ['id'])
    op.create_foreign_key(None, 'booking', 'group_join', ['group_id'], ['id'])
    op.create_foreign_key(None, 'group_join', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'request', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'request', 'machines', ['machine_id'], ['id'])
    op.create_foreign_key(None, 'request', 'request__des', ['requests_id'], ['id'])
    op.create_foreign_key(None, 'request', 'levels', ['level_id'], ['id'])
    op.create_foreign_key(None, 'staff', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'student', 'majors', ['major_id'], ['id'])
    op.create_foreign_key(None, 'student', 'levels', ['level_id'], ['id'])
    op.create_foreign_key(None, 'student', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'student', 'machines', ['machine_id'], ['id'])
    op.create_foreign_key(None, 'student_level', 'levels', ['level_id'], ['id'])
    op.create_foreign_key(None, 'student_level', 'student', ['student_id'], ['id'])
    op.create_foreign_key(None, 'student_level', 'machines', ['machine_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student_level', type_='foreignkey')
    op.drop_constraint(None, 'student_level', type_='foreignkey')
    op.drop_constraint(None, 'student_level', type_='foreignkey')
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_constraint(None, 'staff', type_='foreignkey')
    op.drop_constraint(None, 'request', type_='foreignkey')
    op.drop_constraint(None, 'request', type_='foreignkey')
    op.drop_constraint(None, 'request', type_='foreignkey')
    op.drop_constraint(None, 'request', type_='foreignkey')
    op.drop_constraint(None, 'group_join', type_='foreignkey')
    op.drop_constraint(None, 'booking', type_='foreignkey')
    op.drop_constraint(None, 'booking', type_='foreignkey')
    op.drop_constraint(None, 'booking', type_='foreignkey')
    # ### end Alembic commands ###
