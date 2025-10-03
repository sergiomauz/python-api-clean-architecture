
from dataclasses import dataclass


@dataclass(frozen=True)
class ErrorTuple:
    error_code: str
    property_name: str
    error_message: str