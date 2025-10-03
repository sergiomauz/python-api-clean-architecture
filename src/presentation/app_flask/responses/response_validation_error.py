
import json
from typing import Any
from flask import Response
from pydantic import BaseModel
from application.exceptions.errors import CustomValidationError


class ResponseValidationError(Response):
    def __init__(self, exception:CustomValidationError):
        """ ToDo: DocString """
        if isinstance(exception.details, BaseModel):
            errors = exception.details.model_dump()
        elif isinstance(exception.details, list) and all(isinstance(x, BaseModel) for x in exception.details):
            errors = [x.model_dump() for x in exception.details]
        else:
            errors = exception.details

        response_body = {
            "message": exception.message,
            "errors": errors
        }
        json_str = json.dumps(response_body, ensure_ascii=False)
        super().__init__(
            response=json_str,
            status=exception.code,
            mimetype="application/json"
        )
