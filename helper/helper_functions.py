from enum import Enum


class ReturnCode(Enum):
    STATUS_OK = 0
    STATUS_INVALID = -1
    STATUS_ERROR = -2


def validate_str(name: str) -> ReturnCode:
    if not isinstance(name, str) or len(name.strip()) == 0 or name is None:
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
