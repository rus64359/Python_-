from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    group_name = Column(String(50), nullable=True)
    note = Column(Text, nullable=True)

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name!r})>"