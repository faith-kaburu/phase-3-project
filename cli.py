import click
from sqlalchemy.exc import SQLAlchemyError
from database import SessionLocal, add_student, list_students, get_student_by_id, update_student, delete_student

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.argument('age', type=int)
@click.argument('grade', type=float)
def add_student_command(name, age, grade):
    """Add a new student record."""
    db = SessionLocal()
    try:
        student = add_student(db, name, age, grade)
        db.commit()
        print(f"Added student: ID={student.id}, Name={name}, Age={age}, Grade={grade}")
    except (ValueError, SQLAlchemyError) as e:
        db.rollback()
        print(f"Failed to add the student. Error: {str(e)}")
    finally:
        db.close()

@cli.command()
def list_students_command():
    """List all student records."""
    db = SessionLocal()
    try:
        students = list_students(db)
        if not students:
            print("No students found.")
        else:
            print("List of students (sorted by name):")
            students_sorted = sorted(students, key=lambda x: x.name)
            for student in students_sorted:
                print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
    except SQLAlchemyError as e:
        print(f"An error occurred while listing students. Error: {str(e)}")
    finally:
        db.close()

# Include similar enhancements for other commands (view, update, delete)
# ...