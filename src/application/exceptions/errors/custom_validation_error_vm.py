
from pydantic import BaseModel


class CustomValidationErrorVm(BaseModel):
    property_name: str
    error_code: str
    error_message: str