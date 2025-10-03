import json
from typing import List, Optional, Any
from .custom_validation_error_vm import CustomValidationErrorVm


class CustomValidationError(ValueError):    
    def __init__(self, message:str, errors:Optional[List[CustomValidationErrorVm]], code:int):
        self.message = message
        self.code = code

        if errors:
            grouped: dict[str, list[dict[str, Any]]] = {}
            for err in errors:
                if err.property_name not in grouped:
                    grouped[err.property_name] = []

                grouped[err.property_name].append({
                    "error_code": err.error_code,
                    "error_message": err.error_message
                })

            json_string_errors = json.dumps(grouped, ensure_ascii=False)
            super().__init__(json_string_errors)
            self.details = grouped
        else:
            self.details = {}
            super().__init__(message)
