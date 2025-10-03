from http import HTTPStatus
from typing import Optional, List
from commons.utils import CustomParsers
from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm


class UuidsQuery(CustomValidator):
    
    def __init__(self, ids:Optional[List[str]]=None):
        self.ids = ids

    def format_validation(self):
        errors = []        
        if not self.ids:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.UUIDS_FORMAT00001.error_code,
                property_name=ErrorConstants.UUIDS_FORMAT00001.property_name,                    
                error_message=ErrorConstants.UUIDS_FORMAT00001.error_message
            ))                        
        if len(self.ids) == 0:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.UUIDS_FORMAT00002.error_code,
                property_name=ErrorConstants.UUIDS_FORMAT00002.property_name,                    
                error_message=ErrorConstants.UUIDS_FORMAT00002.error_message
            ))                        
        if len(self.ids) != len(set(self.ids)):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.UUIDS_FORMAT00003.error_code,
                property_name=ErrorConstants.UUIDS_FORMAT00003.property_name,                    
                error_message=ErrorConstants.UUIDS_FORMAT00003.error_message
            ))                                    
        if not CustomParsers.are_valid_uuids(self.ids):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.UUIDS_FORMAT00004.error_code,
                property_name=ErrorConstants.UUIDS_FORMAT00004.property_name,                    
                error_message=ErrorConstants.UUIDS_FORMAT00004.error_message
            ))    
                        
        if errors:
            raise CustomValidationError(
                None, 
                errors, 
                HTTPStatus.UNPROCESSABLE_ENTITY.value)   

        return errors