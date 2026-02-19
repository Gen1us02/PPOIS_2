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
