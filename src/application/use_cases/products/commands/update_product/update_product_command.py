from http import HTTPStatus
from application.commons.queries import IdQuery
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .update_product_route import UpdateProductRoute
from .update_product_dto import UpdateProductDto


class UpdateProductCommand(IdQuery):

    def __init__(self, route:UpdateProductRoute, dto:UpdateProductDto):
        super().__init__(id=route.id if route else dto.id)
        self.category_id = dto.category_id
        self.code = dto.code
        self.name = dto.name
        self.description = dto.description

    def format_validation(self):
        errors = super().format_validation()
        if self.category_id is not None and (not isinstance(self.category_id, int) or self.category_id < 1):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.UPDATE_PRODUCT_FORMAT00001.error_code,
                property_name=ErrorConstants.UPDATE_PRODUCT_FORMAT00001.property_name,                    
                error_message=ErrorConstants.UPDATE_PRODUCT_FORMAT00001.error_message
            ))        
        if self.code is not None and (len(self.code) < 5 or len(self.code) > 10):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.UPDATE_PRODUCT_FORMAT00002.error_code,
                property_name=ErrorConstants.UPDATE_PRODUCT_FORMAT00002.property_name,                    
                error_message=ErrorConstants.UPDATE_PRODUCT_FORMAT00002.error_message
            ))            
        if self.name is not None and (len(self.name) < 3 or len(self.name) > 75):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.UPDATE_PRODUCT_FORMAT00003.error_code,
                property_name=ErrorConstants.UPDATE_PRODUCT_FORMAT00003.property_name,                    
                error_message=ErrorConstants.UPDATE_PRODUCT_FORMAT00003.error_message
            ))
        if self.description is not None and (len(self.description) < 3 or len(self.description) > 150):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.UPDATE_PRODUCT_FORMAT00004.error_code,
                property_name=ErrorConstants.UPDATE_PRODUCT_FORMAT00004.property_name,                    
                error_message=ErrorConstants.UPDATE_PRODUCT_FORMAT00004.error_message
            ))
                
        if errors:
            raise CustomValidationError(
                None,
                errors,
                HTTPStatus.UNPROCESSABLE_ENTITY.value
            )

        return errors
