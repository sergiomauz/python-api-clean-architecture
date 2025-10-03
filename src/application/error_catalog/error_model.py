
from dataclasses import dataclass


@dataclass
class ErrorModel:
    error_code: str
    error_message: str
    property_name: str