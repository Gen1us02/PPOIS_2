from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy import CheckConstraint, ForeignKey, String, UniqueConstraint
from typing import List, Optional


class Base(DeclarativeBase):
    pass


class Subject(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)


class Group(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str] = mapped_column(String(6), unique=True, nullable=False)
    students: Mapped[List["Student"]] = relationship(back_populates="group")
    __table_args__ = (
        CheckConstraint(
            "length(number) = 6 AND number ~ '^[1-9][0-9]{5}$'",
            name="valid_group_number",
        ),
    )


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    middle_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id", ondelete="CASCADE"))
    group: Mapped["Group"] = relationship(back_populates="students")
    scores: Mapped[List["Score"]] = relationship(back_populates="student")
    
    @property
    def full_name(self) -> str:
        parts = [self.last_name, self.first_name]
        if self.middle_name:
            parts.append(self.middle_name)
        return " ".join(parts)


class Exam(Base):
    __tablename__ = "exams"
    id: Mapped[int] = mapped_column(primary_key=True)
    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subjects.id", ondelete="CASCADE")
    )
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id", ondelete="CASCADE"))
    subject: Mapped["Subject"] = relationship()
    group: Mapped["Group"] = relationship()
    scores: Mapped[List["Score"]] = relationship(back_populates="exam")
    __table_args__ = (
        UniqueConstraint("group_id", "subject_id", name="unique_subject_per_group"),
    )


class Score(Base):
    __tablename__ = "scores"
    id: Mapped[int] = mapped_column(primary_key=True)
    exam_id: Mapped[int] = mapped_column(ForeignKey("exams.id", ondelete="CASCADE"))
    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE")
    )
    grade: Mapped[int]
    exam: Mapped["Exam"] = relationship(back_populates="scores")
    student: Mapped["Student"] = relationship(back_populates="scores")
    __table_args__ = (
        UniqueConstraint("student_id", "exam_id", name="unique_student_grade"),
        CheckConstraint("grade BETWEEN 1 AND 10", name="valid_grade"),
    )
