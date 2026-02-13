from datetime import datetime
from .validator import Validator
from exceptions.exceptions import SoftwareException


class Software:
    def __init__(self, version: str, name: str) -> None:
        self.__set_version(version)
        self.name = name
        self.last_update = datetime.now()

    def __set_version(self, version: str) -> None:
        if not Validator.validate_version(version):
            raise SoftwareException("Невалидная версия")

        self.version = version

    def update(self, new_version: str) -> None:
        if not Validator.validate_version(new_version):
            raise SoftwareException("Невалидная версия")

        if Validator.compare_versions(self.version, new_version):
            raise SoftwareException("Текущая версия актуальнее")

        self.version = new_version
        self.last_update = datetime.now()
