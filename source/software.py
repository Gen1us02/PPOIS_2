import datetime
from source.utils import compare_versions, validate_version
from exceptions.exceptions import SoftwareException


class Software:
    def __init__(self, version: str, name: str) -> None:
        self.version = version
        self.name = name
        self.last_update = datetime.now()

    def update(self, new_version: str) -> None:
        if not validate_version(new_version):
            raise SoftwareException("Incorrect version")

        if compare_versions(self.version, new_version):
            raise SoftwareException("Current version is greater then new")

        self.version = new_version
        self.last_update = datetime.now()
