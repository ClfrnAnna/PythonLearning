"""init tables

Revision ID: f04519f3daa3
Revises: 
Create Date: 2023-05-20 15:26:37.372817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f04519f3daa3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__group'))
    )
    op.create_table('teacher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('second_name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__teacher'))
    )
    op.create_table('lesson',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('theme', sa.String(length=50), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], name=op.f('fk__lesson__group_id__group')),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], name=op.f('fk__lesson__teacher_id__teacher')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__lesson'))
    )
    op.create_index(op.f('ix__lesson__group_id'), 'lesson', ['group_id'], unique=False)
    op.create_index(op.f('ix__lesson__teacher_id'), 'lesson', ['teacher_id'], unique=False)
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('second_name', sa.String(length=255), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], name=op.f('fk__student__group_id__group')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__student'))
    )
    op.create_index(op.f('ix__student__group_id'), 'student', ['group_id'], unique=False)
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=40), nullable=False),
    sa.Column('difficulty_level', sa.SmallInteger(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['lesson_id'], ['lesson.id'], name=op.f('fk__task__lesson_id__lesson')),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], name=op.f('fk__task__student_id__student')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__task'))
    )
    op.create_index(op.f('ix__task__lesson_id'), 'task', ['lesson_id'], unique=False)
    op.create_index(op.f('ix__task__student_id'), 'task', ['student_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix__task__student_id'), table_name='task')
    op.drop_index(op.f('ix__task__lesson_id'), table_name='task')
    op.drop_table('task')
    op.drop_index(op.f('ix__student__group_id'), table_name='student')
    op.drop_table('student')
    op.drop_index(op.f('ix__lesson__teacher_id'), table_name='lesson')
    op.drop_index(op.f('ix__lesson__group_id'), table_name='lesson')
    op.drop_table('lesson')
    op.drop_table('teacher')
    op.drop_table('group')
    # ### end Alembic commands ###
