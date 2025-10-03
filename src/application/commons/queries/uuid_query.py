from commons.utils import CustomParsers
from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationErrorVm


class UuidQuery(CustomValidator):

    def __init__(self, id:str):
        self.id = id
        
    def format_validation(self):
        errors = []        
        if not CustomParsers.is_valid_uuid(self.id):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.UUID_FORMAT00001.error_code,
                property_name=ErrorConstants.UUID_FORMAT00001.property_name,                    
                error_message=ErrorConstants.UUID_FORMAT00001.error_message
            ))

        return errors
