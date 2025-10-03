from typing import Dict, List
from pydantic import BaseModel, Field


class Response409Vm(BaseModel):
    class ExceptionDetails(BaseModel):
        error_code: str
        error_message: str
    
    exceptions: Dict[str, List[ExceptionDetails]] = Field(
        ...,
        example={
            "field_one": [
                {
                    "error_code": "string",
                    "error_message": "string"
                }
            ]
        }
    )