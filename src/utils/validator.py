from typing import Any, Dict, List


class Validator:
    @staticmethod
    def validate_fio_part(fio_part: str) -> bool:
        if Validator.is_empty(fio_part):
            return False

        if Validator.contains_number(fio_part):
            return False

        return True

    @staticmethod
    def is_empty(string: str) -> bool:
        return not string

    @staticmethod
    def contains_number(string: str) -> bool:
        return any(ch in "0123456789" for ch in string)

    @staticmethod
    def score_validation(number: int) -> bool:
        return 4 <= number <= 10

    @staticmethod
    def validate_xml(
        students_data: List[Dict[str, Any]], groups: List[str], exams: List[str]
    ) -> bool:
        for data in students_data:
            first_name = data.get("first_name", None)
            last_name = data.get("last_name", None)
            middle_name = data.get("middle_name", "")
            group = data.get("group", None)
            scores = data.get("scores", None)

            if not first_name or not Validator.validate_fio_part(first_name):
                return False

            if not last_name or not Validator.validate_fio_part(last_name):
                return False

            if Validator.contains_number(middle_name):
                return False

            if group not in groups:
                return False

            for exam, grade in scores.items():
                if not exam or exam not in exams:
                    return False

                if not Validator.score_validation(grade):
                    return False

        return True
