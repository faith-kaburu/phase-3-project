import click
from sqlalchemy.orm import Session
from database import init_db, SessionLocal
from student import add_student, list_students, get_student_by_id, update_student, delete_student
from course import add_course, list_courses, get_course_by_id, update_course, delete_course
from enrollment import enroll_student, list_enrollments, get_enrollment_by_id, update_enrollment, delete_enrollment

@click.group()
def cli():
    pass

# Student commands
@cli.command()
@click.argument('name')
@click.argument('age', type=int)
@click.argument('grade', type=float)
def add_student_command(name, age, grade):
    """Add a new student record."""
    db = SessionLocal()
    student = add_student(db, name, age, grade)
    db.close()
    if student:
        print(f"Added student: ID={student.id}, Name={name}, Age={age}, Grade={grade}")
    else:
        print("Failed to add the student.")

@cli.command()
def list_students_command():
    """List all student records."""
    db = SessionLocal()
    students = list_students(db)
    db.close()
    if not students:
        print("No students found.")
        return

    print("List of students (sorted by name):")
    students_sorted = sorted(students, key=lambda x: x.name)
    for student in students_sorted:
        student_dict = {
            "ID": student.id,
            "Name": student.name,
            "Age": student.age,
            "Grade": student.grade
        }
        print(student_dict)

@cli.command()
@click.argument('student_id', type=int)
def view_student_command(student_id):
    """View details of a specific student by ID."""
    db = SessionLocal()
    student = get_student_by_id(db, student_id)
    db.close()
    if student:
        print(f"Student ID: {student.id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
    else:
        print(f"Student with ID {student_id} not found.")

@cli.command()
@click.argument('student_id', type=int)
@click.argument('name')
@click.argument('age', type=int)
@click.argument('grade', type=float)
def update_student_command(student_id, name, age, grade):
    """Update student record details."""
    db = SessionLocal()
    updated_student = update_student(db, student_id, name, age, grade)
    db.close()
    if updated_student:
        print(f"Updated student: ID={student_id}, Name={name}, Age={age}, Grade={grade}")
    else:
        print(f"Student with ID {student_id} not found.")

@cli.command()
@click.argument('student_id', type=int)
def delete_student_command(student_id):
    """Delete a student record by ID."""
    db = SessionLocal()
    if delete_student(db, student_id):
        print(f"Deleted student with ID {student_id}")
    else:
        print(f"Student with ID {student_id} not found.")

# Course commands
@cli.command()
@click.argument('name')
def add_course_command(name):
    """Add a new course."""
    db = SessionLocal()
    course = add_course(db, name)
    db.close()
    if course:
        print(f"Added course: ID={course.id}, Name={name}")
    else:
        print("Failed to add the course.")

@cli.command()
def list_courses_command():
    """List all courses."""
    db = SessionLocal()
    courses = list_courses(db)
    db.close()
    if not courses:
        print("No courses found.")
        return

    print("List of courses:")
    for course in courses:
        course_dict = {
            "ID": course.id,
            "Name": course.name
        }
        print(course_dict)

@cli.command()
@click.argument('course_id', type=int)
def view_course_command(course_id):
    """View details of a specific course by ID."""
    db = SessionLocal()
    course = get_course_by_id(db, course_id)
    db.close()
    if course:
        print(f"Course ID: {course.id}, Name: {course.name}")
    else:
        print(f"Course with ID {course_id} not found.")

@cli.command()
@click.argument('course_id', type=int)
@click.argument('name')
def update_course_command(course_id, name):
    """Update course details."""
    db = SessionLocal()
    updated_course = update_course(db, course_id, name)
    db.close()
    if updated_course:
        print(f"Updated course: ID={course_id}, Name={name}")
    else:
        print(f"Course with ID {course_id} not found.")

@cli.command()
@click.argument('course_id', type=int)
def delete_course_command(course_id):
    """Delete a course by ID."""
    db = SessionLocal()
    if delete_course(db, course_id):
        print(f"Deleted course with ID {course_id}")
    else:
        print(f"Course with ID {course_id} not found.")

# Enrollment commands
@cli.command()
@click.argument('student_id', type=int)
@click.argument('course_id', type=int)
@click.argument('grade', type=float)
def enroll_student_command(student_id, course_id, grade):
    """Enroll a student in a course and assign a grade."""
    db = SessionLocal()
    enrollment = enroll_student(db, student_id, course_id, grade)
    db.close()
    if enrollment:
        print(f"Enrolled student ID={student_id} in course ID={course_id} with grade={grade}")
    else:
        print("Failed to enroll the student.")

@cli.command()
@click.argument('student_id', type=int)
@click.argument('course_id', type=int)
def view_enrollment_command(student_id, course_id):
    """View enrollment details for a student in a course."""
    db = SessionLocal()
    enrollment = get_enrollment_by_id(db, student_id, course_id)
    db.close()
    if enrollment:
        print(f"Enrollment - Student ID: {student_id}, Course ID: {course_id}, Grade: {enrollment.grade}")
    else:
        print(f"Enrollment not found for Student ID {student_id} in Course ID {course_id}.")

@cli.command()
@click.argument('student_id', type=int)
@click.argument('course_id', type=int)
@click.argument('grade', type=float)
def update_enrollment_command(student_id, course_id, grade):
    """Update an enrollment record for a student in a course."""
    db = SessionLocal()
    updated_enrollment = update_enrollment(db, student_id, course_id, grade)
    db.close()
    if updated_enrollment:
        print(f"Updated enrollment - Student ID: {student_id}, Course ID: {course_id}, Grade: {grade}")
    else:
        print(f"Enrollment not found for Student ID {student_id} in Course ID {course_id}.")

@cli.command()
@click.argument('student_id', type=int)
@click.argument('course_id', type=int)
def delete_enrollment_command(student_id, course_id):
    """Delete an enrollment record for a student in a course."""
    db = SessionLocal()
    if delete_enrollment(db, student_id, course_id):
        print(f"Deleted enrollment - Student ID: {student_id}, Course ID: {course_id}")
    else:
        print(f"Enrollment not found for Student ID {student_id} in Course ID {course_id}.")

if __name__ == '__main__':
    init_db()
    cli()
