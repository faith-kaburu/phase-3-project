from sqlalchemy.orm import Session
from models import Course

def add_course(db: Session, name: str) -> Course:
    """Add a new course with details like course name."""
    course = Course(name=name)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def list_courses(db: Session):
    """List all available courses."""
    return db.query(Course).all()

def get_course_by_id(db: Session, course_id: int):
    """View details of a specific course by ID."""
    return db.query(Course).filter(Course.id == course_id).first()

def update_course(db: Session, course_id: int, name: str):
    """Update course information."""
    course = db.query(Course).filter(Course.id == course_id).first()
    if course:
        course.name = name
        db.commit()
        db.refresh(course)
    return course

def delete_course(db: Session, course_id: int) -> bool:
    """Delete a course by ID."""
    course = db.query(Course).filter(Course.id == course_id).first()
    if course:
        db.delete(course)
        db.commit()
        return True
    return False
