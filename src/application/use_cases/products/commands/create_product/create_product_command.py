from http import HTTPStatus
from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .create_product_dto import CreateProductDto


class CreateProductCommand(CustomValidator):

    def __init__(self, dto:CreateProductDto):
        self.category_id = dto.category_id
        self.code = dto.code
        self.name = dto.name
        self.description = dto.description

    def format_validation(self):
        errors = []
        if not self.category_id or not isinstance(self.category_id, int) or self.category_id < 1:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_PRODUCT_FORMAT00001.error_code,
                property_name=ErrorConstants.CREATE_PRODUCT_FORMAT00001.property_name,                    
                error_message=ErrorConstants.CREATE_PRODUCT_FORMAT00001.error_message
            ))        
        if not self.code or len(self.code) < 5 or len(self.code) > 10:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_PRODUCT_FORMAT00002.error_code,
                property_name=ErrorConstants.CREATE_PRODUCT_FORMAT00002.property_name,                    
                error_message=ErrorConstants.CREATE_PRODUCT_FORMAT00002.error_message
            ))            
        if not self.name or len(self.name) < 3 or len(self.name) > 75:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_PRODUCT_FORMAT00003.error_code,
                property_name=ErrorConstants.CREATE_PRODUCT_FORMAT00003.property_name,                    
                error_message=ErrorConstants.CREATE_PRODUCT_FORMAT00003.error_message
            ))
        if not self.description or len(self.description) < 3 or len(self.description) > 150:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_PRODUCT_FORMAT00004.error_code,
                property_name=ErrorConstants.CREATE_PRODUCT_FORMAT00004.property_name,                    
                error_message=ErrorConstants.CREATE_PRODUCT_FORMAT00004.error_message
            ))

        if errors:
            raise CustomValidationError(
                None,
                errors,
                HTTPStatus.UNPROCESSABLE_ENTITY.value
            )

        return errors