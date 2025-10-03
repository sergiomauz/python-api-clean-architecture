
from typing import Any
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from .remove_nones import remove_nones

    
class ResponseOk(JSONResponse):
    def __init__(self, message:str, vm:Any):
        """ ToDo: DocString """
        if isinstance(vm, BaseModel):
            data = vm.model_dump(exclude_none=True)
        elif isinstance(vm, list) and all(isinstance(x, BaseModel) for x in vm):
            data = [x.model_dump(exclude_none=True) for x in vm]
        else:
            data = remove_nones(vm)

        content = {
            "message": message,
            "data": data
        }

        super().__init__(content=content, status_code=200)
