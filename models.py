# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship, validates

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'  # Corrected attribute name

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True, nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(Float, nullable=False)

    # Added validation for age and grade
    @validates('age')
    def validate_age(self, key, value):
        if not (0 <= value <= 150):
            raise ValueError("Age must be between 0 and 150.")
        return value

    @validates('grade')
    def validate_grade(self, key, value):
        if not (0.0 <= value <= 100.0):
            raise ValueError("Grade must be between 0.0 and 100.0.")
        return value

    enrollments = relationship('Enrollment', back_populates='student')

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)

    enrollments = relationship('Enrollment', back_populates='course')

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    grade = Column(Float)

    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')
