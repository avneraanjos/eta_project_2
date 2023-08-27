from enum import Enum


class ReturnCode(Enum):
    STATUS_OK = 0
    STATUS_NONE = -1
    STATUS_INVALID = -2
    STATUS_ERROR = -3


def validate_name(name: str) -> ReturnCode:
    if not isinstance(name, str) or name == '':
        return ReturnCode.STATUS_INVALID
    else:
        return ReturnCode.STATUS_OK


def validate_number(number: int) -> bool:
    if isinstance(number, int) and number > 0:
        return True
    else:
        return False


def is_ok(status: ReturnCode) -> bool:
    return status == ReturnCode.STATUS_OK
