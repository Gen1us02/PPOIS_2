from typing import Optional


class DeviceException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class SensorException(DeviceException):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class MechanismException(DeviceException):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class BatteryException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class SoftwareException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class RobotException(Exception):
    def __init__(self, message: str, exception: Optional[Exception] = None) -> None:
        if exception:
            full_message = f"{message}{exception}"
        else:
            full_message = message
        super().__init__(full_message)
        self.original_exception = exception


class ControlSystemException(Exception):
    def __init__(self, message: str, exception: Optional[Exception] = None) -> None:
        if exception:
            full_message = f"{message}{exception}"
        else:
            full_message = message
        super().__init__(full_message)
        self.original_exception = exception
