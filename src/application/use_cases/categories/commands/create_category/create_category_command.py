from http import HTTPStatus
from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .create_category_dto import CreateCategoryDto


class CreateCategoryCommand(CustomValidator):    

    def __init__(self, dto:CreateCategoryDto):
        self.name = dto.name
        self.description = dto.description
        
    def format_validation(self):
        errors = []        
        if not self.name or (len(self.name) < 3 or len(self.name) > 75):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_CATEGORY_FORMAT00001.error_code,
                property_name=ErrorConstants.CREATE_CATEGORY_FORMAT00001.property_name,                    
                error_message=ErrorConstants.CREATE_CATEGORY_FORMAT00001.error_message
            ))
        if not self.description or (len(self.description) < 3 or len(self.description) > 150):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_CATEGORY_FORMAT00002.error_code,
                property_name=ErrorConstants.CREATE_CATEGORY_FORMAT00002.property_name,                    
                error_message=ErrorConstants.CREATE_CATEGORY_FORMAT00002.error_message
            ))

        if errors:
            raise CustomValidationError(
                None,
                errors, 
                HTTPStatus.UNPROCESSABLE_ENTITY.value
            )

        return errors