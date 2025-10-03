
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from application.exceptions.errors import CustomValidationError


class ResponseValidationError(JSONResponse):

    def __init__(self, exception:CustomValidationError):
        if isinstance(exception.details, BaseModel):
            errors = exception.details.model_dump()
        elif isinstance(exception.details, list) and all(isinstance(x, BaseModel) for x in exception.details):
            errors = [x.model_dump() for x in exception.details]
        else:
            errors = exception.details

        content = {}
        if errors:
            content["exceptions"] = errors        
        if exception.message:
            content["message"] = exception.message

        super().__init__(content=content, status_code=exception.code)
