from typing import List
import xml.dom.minidom as minidom
from src.db.models import Student


class XMLWriter:
    @staticmethod
    def save_to_file(students: List[Student], filename: str) -> None:
        doc = minidom.Document()
        students_elem = doc.createElement("students")
        doc.appendChild(students_elem)

        for student in students:
            student_elem = doc.createElement("student")
            student_elem.setAttribute("group", student.group.number)
            student_elem.setAttribute("first_name", student.first_name)
            student_elem.setAttribute("last_name", student.last_name)
            if student.middle_name:
                student_elem.setAttribute("middle_name", student.middle_name)
            students_elem.appendChild(student_elem)

            scores_elem = doc.createElement("scores")
            student_elem.appendChild(scores_elem)

            for score in student.scores:
                score_elem = doc.createElement("score")
                score_elem.setAttribute("subject", score.exam.subject.name)
                score_elem.setAttribute("grade", str(score.grade))
                scores_elem.appendChild(score_elem)

        with open(filename, "w", encoding="utf-8") as f:
            doc.writexml(f, indent="  ", addindent="  ", newl="\n", encoding="utf-8")
