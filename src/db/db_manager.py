from typing import List
from sqlalchemy.orm import Session, selectinload, sessionmaker
from sqlalchemy import and_, exists, func, select, delete
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

    def get_all_subjects(self) -> List[str]:
        with self.session() as session:
            stmt = select(Subject.name)
            subjects = session.scalars(stmt).all()

            return subjects

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

    def __get_group_id(self, group_number: str, session: Session) -> int:
        with session:
            statement = select(Group.id).where(Group.number == group_number)
            group_id = session.scalars(statement).one()

            return group_id

    def __get_exam_id(self, exam: str, group_id: int, session: Session) -> int:
        with session:
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
            group_id = self.__get_group_id(kwargs["group_name"], session)
            new_student = Student(
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                group_id=group_id,
            )
            session.add(new_student)
            session.flush()
            for exam, score in kwargs["scores"].items():
                exam_id = self.__get_exam_id(exam, group_id, session)
                student_id = new_student.id
                student_score = Score(
                    exam_id=exam_id, student_id=student_id, grade=score
                )
                session.add(student_score)

            session.commit()

    def search_students(self, **kwargs) -> List[Student]:
        with self.session() as session:
            subject = kwargs.get("subject")
            group = kwargs.get("group")
            avg_min = kwargs.get("avg_min")
            avg_max = kwargs.get("avg_max")
            rating_min = kwargs.get("rating_min")
            rating_max = kwargs.get("rating_max")

            statement = select(Student).options(
                selectinload(Student.group),
                selectinload(Student.scores)
                .selectinload(Score.exam)
                .selectinload(Exam.subject),
            ).distinct()

            if group:
                statement = statement.join(Student.group).where(Group.number == group)

            if subject:
                rating_sbq = (
                    select(Score)
                    .join(Score.exam)
                    .join(Exam.subject)
                    .where(Subject.name == subject)
                    .subquery()
                )

                conditions = []
                if rating_min:
                    conditions.append(rating_sbq.c.grade >= rating_min)
                if rating_max:
                    conditions.append(rating_sbq.c.grade <= rating_max)

                if conditions:
                    rating_cond = and_(*conditions)
                    statement = statement.where(
                        exists().where(
                            (rating_sbq.c.student_id == Student.id) & rating_cond
                        )
                    )

            if avg_min or avg_max:
                avg_sbq = (
                    select(Score.student_id, func.avg(Score.grade).label("avg_grade"))
                    .group_by(Score.student_id)
                    .subquery()
                )

                conditions = []
                if avg_min:
                    conditions.append(avg_sbq.c.avg_grade >= avg_min)
                if avg_max:
                    conditions.append(avg_sbq.c.avg_grade <= avg_max)

                if conditions:
                    statement = statement.join(
                        avg_sbq, avg_sbq.c.student_id == Student.id
                    ).where(*conditions)

            return session.scalars(statement).all()

    def delete_students(self, **kwargs) -> int:
        with self.session() as session:
            students = self.search_students(**kwargs)
            student_ids = [s.id for s in students]

            deleted_students = len(students)

            session.execute(delete(Student).where(Student.id.in_(student_ids)))

            session.commit()

            return deleted_students
