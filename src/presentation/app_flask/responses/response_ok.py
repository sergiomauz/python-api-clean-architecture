
import json
from typing import Any
from flask import Response
from pydantic import BaseModel


class ResponseOk(Response):
    def __init__(self, message:str, vm:Any):
        """ ToDo: DocString """
        if isinstance(vm, BaseModel):
            data = vm.model_dump()
        elif isinstance(vm, list) and all(isinstance(x, BaseModel) for x in vm):
            data = [x.model_dump() for x in vm]
        else:
            data = vm

        response_body = {
            "message": message,
            "data": data
        }
        json_str = json.dumps(response_body, ensure_ascii=False)
        super().__init__(
            response=json_str,
            status=200,
            mimetype="application/json"
        )
