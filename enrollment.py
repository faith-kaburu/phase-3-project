from sqlalchemy.orm import Session
from models import Enrollment

def list_enrollments(db: Session):
    """List all enrollments."""
    return db.query(Enrollment).all()


def get_enrollment_by_id(db: Session, enrollment_id: int):
    """Get enrollment details by enrollment ID."""
    return db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()

def enroll_student(db: Session, student_id: int, course_id: int, grade: float):
    """Enroll students in courses and assign grades."""
    enrollment = Enrollment(student_id=student_id, course_id=course_id, grade=grade)
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

def get_enrollments_by_student_id(db: Session, student_id: int):
    """View enrollments for an individual student."""
    return db.query(Enrollment).filter(Enrollment.student_id == student_id).all()

def get_enrollments_by_course_id(db: Session, course_id: int):
    """View enrollments for a specific course."""
    return db.query(Enrollment).filter(Enrollment.course_id == course_id).all()

def update_enrollment(db: Session, enrollment_id: int, grade: float):
    """Update enrollment details (e.g., grades)."""
    enrollment = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
    if enrollment:
        enrollment.grade = grade
        db.commit()
        db.refresh(enrollment)
    return enrollment

def delete_enrollment(db: Session, enrollment_id: int) -> bool:
    """Delete an enrollment by ID."""
    enrollment = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
    if enrollment:
        db.delete(enrollment)
        db.commit()
        return True
    return False
