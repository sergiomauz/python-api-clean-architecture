from http import HTTPStatus
from typing import Optional, List
from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm


class IdsQuery(CustomValidator):
    
    def __init__(self, ids:Optional[List[int]]=None):
        self.ids = ids

    def format_validation(self):
        errors = []        
        if not self.ids:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.IDS_FORMAT00001.error_code,
                property_name=ErrorConstants.IDS_FORMAT00001.property_name,                    
                error_message=ErrorConstants.IDS_FORMAT00001.error_message
            ))                        
        if len(self.ids) == 0:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.IDS_FORMAT00002.error_code,
                property_name=ErrorConstants.IDS_FORMAT00002.property_name,                    
                error_message=ErrorConstants.IDS_FORMAT00002.error_message
            ))                        
        if len(self.ids) != len(set(self.ids)):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.IDS_FORMAT00003.error_code,
                property_name=ErrorConstants.IDS_FORMAT00003.property_name,                    
                error_message=ErrorConstants.IDS_FORMAT00003.error_message
            ))                                    
        if not all(id > 0 for id in self.ids):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.IDS_FORMAT00004.error_code,
                property_name=ErrorConstants.IDS_FORMAT00004.property_name,                    
                error_message=ErrorConstants.IDS_FORMAT00004.error_message
            ))            
            
        if errors:
            raise CustomValidationError(
                None, 
                errors, 
                HTTPStatus.UNPROCESSABLE_ENTITY.value)   

        return errors