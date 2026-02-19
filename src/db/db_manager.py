from typing import Dict, List
from sqlalchemy.orm import selectinload, sessionmaker
from sqlalchemy import select
from .models import Exam, Group, Score, Student, Subject
from .settings import engine


class DBManager:
    def __init__(self):
        self.session = sessionmaker(bind=engine)

    def get_all_records(self) -> List[Student]:
        with self.session() as session:
            statement = select(Student).options(
                selectinload(Student.group),
                selectinload(Student.scores)
                .selectinload(Score.exam)
                .selectinload(Exam.subject),
            )
            all_records = session.scalars(statement).all()

            return all_records

    def get_groups_exams(self) -> Dict[int, List[str]]:
        with self.session() as session:
            stmt = (
                select(Exam.group_id, Subject.name)
                .join(Subject, Exam.subject_id == Subject.id)
                .order_by(Exam.group_id, Subject.name)
            )
            rows = session.execute(stmt).all()
            exams_per_group = {}
            for group_id, name in rows:
                exams_per_group.setdefault(group_id, []).append(name)
            return exams_per_group

    def get_all_groups(self) -> List[str]:
        with self.session() as session:
            statement = select(Group.number)
            groups = session.scalars(statement).all()

            return groups

    def get_all_exams_in_group(self, group: str) -> List[str]:
        with self.session() as session:
            group_id_subq = (
                select(Group.id).where(Group.number == group).scalar_subquery()
            )
            statement = (
                select(Subject.name)
                .join(Exam, Exam.subject_id == Subject.id)
                .where(Exam.group_id == group_id_subq)
            )
            exams = session.scalars(statement).all()

            return exams

    def __get_group_id(self, group_number: str) -> int:
        with self.session() as session:
            statement = select(Group.id).where(Group.number == group_number)
            group_id = session.scalars(statement).one()

            return group_id

    def __get_exam_id(self, exam: str, group_id: int) -> int:
        with self.session() as session:
            statement = (
                select(Exam.id)
                .join(Subject, Exam.subject_id == Subject.id)
                .where(Subject.name == exam, Exam.group_id == group_id)
            )
            exam_id = session.scalars(statement).one()

            return exam_id

    def add_student(self, **kwargs) -> None:
        with self.session() as session:
            first_name = kwargs["first_name"]
            last_name = kwargs["last_name"]
            middle_name = kwargs["middle_name"]
            group_id = self.__get_group_id(kwargs["group_name"])
            new_student = Student(
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                group_id=group_id,
            )
            session.add(new_student)
            session.flush()
            for exam, score in kwargs["scores"].items():
                exam_id = self.__get_exam_id(exam, group_id)
                student_id = new_student.id
                student_score = Score(
                    exam_id=exam_id, student_id=student_id, grade=score
                )
                session.add(student_score)

            session.commit()
