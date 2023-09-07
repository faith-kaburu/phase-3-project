"""initial migration

Revision ID: 4626497e544d
Revises: 
Create Date: 2023-09-07 15:26:39.821041

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4626497e544d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.create_table(
        'students',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('age', sa.Integer(), nullable=False),
        sa.Column('grade', sa.Float(), nullable=False),
    )
     op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False, unique=True),
    )

     op.create_table(
        'enrollments',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), nullable=False),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), nullable=False),
        sa.Column('grade', sa.Float()),
    )

def downgrade() -> None:
     op.drop_table('enrollments')
     op.drop_table('courses')
     op.drop_table('students') 
