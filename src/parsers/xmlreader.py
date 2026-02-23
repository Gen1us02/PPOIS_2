from typing import Any, Dict, List
import xml.sax
from xml.sax.handler import ContentHandler
from src.db.db_manager import DBManager


class StudentsHendler(ContentHandler):
    def __init__(self) -> None:
        self.students = []
        self.current_student = None

    def startElement(self, name, attrs):
        if name == "student":
            try:
                self.current_student = {
                    "first_name": attrs.getValue("first_name"),
                    "last_name": attrs.getValue("last_name"),
                    "middle_name": attrs.get("middle_name", ""),
                    "group": attrs.getValue("group"),
                    "scores": {},
                }
            except KeyError as e:
                print(f"Пропущен ключ {e}")
                self.current_student = None

        elif name == "score" and self.current_student:
            try:
                subject = attrs.getValue("subject")
                grade = int(attrs.getValue("grade"))
                self.current_student["scores"][subject] = grade
            except (KeyError, ValueError) as e:
                print(f"Ошибка добавления оценки студента: {e}")

    def endElement(self, name):
        if name == "student":
            if self.current_student:
                self.students.append(self.current_student)


class XMLReader:
    @staticmethod
    def __parse_file(filename: str) -> List[Dict[str, Any]]:
        handler = StudentsHendler()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        try:
            parser.parse(filename)
        except Exception as e:
            print(f"Ошибка парсинга файла: {e}")
            return []

        return handler.students

    @staticmethod
    def add_students_from_xml(filename: str, db: DBManager) -> None:
        students_data = XMLReader.__parse_file(filename)

        for data in students_data:
            students_data = {
                "first_name": data["first_name"],
                "last_name": data["last_name"],
                "middle_name": data["middle_name"],
                "group_name": data["group"],
                "scores": data["scores"],
            }
            db.add_student(**students_data)
