from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationErrorVm


class IdQuery(CustomValidator):

    def __init__(self, id:int):
        self.id = id
        
    def format_validation(self):
        errors = []        
        if self.id is None:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.ID_FORMAT00001.error_code,
                property_name=ErrorConstants.ID_FORMAT00001.property_name,                    
                error_message=ErrorConstants.ID_FORMAT00001.error_message
            ))
        if self.id is not None and self.id < 1:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.ID_FORMAT00002.error_code,
                property_name=ErrorConstants.ID_FORMAT00002.property_name,                    
                error_message=ErrorConstants.ID_FORMAT00002.error_message
            ))

        return errors
