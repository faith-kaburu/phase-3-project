from sqlalchemy.orm import Session
from models import Student

def add_student(db: Session, name: str, age: int, grade: float) -> Student:
    """Add a new student record to the database."""
    student = Student(name=name, age=age, grade=grade)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def list_students(db: Session):
    """List all student records."""
    return db.query(Student).all()

def get_student_by_id(db: Session, student_id: int):
    """View details of a specific student by ID."""
    return db.query(Student).filter(Student.id == student_id).first()

def get_student_by_name(db: Session, name: str):
    """View details of a specific student by name."""
    return db.query(Student).filter(Student.name == name).first()

def update_student(db: Session, student_id: int, name: str, age: int, grade: float):
    """Update student record details."""
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        student.name = name
        student.age = age
        student.grade = grade
        db.commit()
        db.refresh(student)
    return student

def delete_student(db: Session, student_id: int) -> bool:
    """Delete a student record by ID."""
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
        return True
    return False
