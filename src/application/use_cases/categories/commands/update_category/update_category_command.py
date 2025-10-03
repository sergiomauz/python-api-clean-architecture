from http import HTTPStatus
from application.commons.queries import IdQuery
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .update_category_route import UpdateCategoryRoute
from .update_category_dto import UpdateCategoryDto


class UpdateCategoryCommand(IdQuery):
        
    def __init__(self, route:UpdateCategoryRoute, dto:UpdateCategoryDto):
        super().__init__(id=route.id if route else dto.id)
        self.name = dto.name
        self.description = dto.description

    def format_validation(self):        
        errors = super().format_validation()
        if self.name is not None  and (len(self.name) < 3 or len(self.name) > 75):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.UPDATE_CATEGORY_FORMAT00001.error_code,
                property_name=ErrorConstants.UPDATE_CATEGORY_FORMAT00001.property_name,                    
                error_message=ErrorConstants.UPDATE_CATEGORY_FORMAT00001.error_message
            ))        
        if self.description is not None  and (len(self.description) < 3 or len(self.description) > 150):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.UPDATE_CATEGORY_FORMAT00002.error_code,
                property_name=ErrorConstants.UPDATE_CATEGORY_FORMAT00002.property_name,                    
                error_message=ErrorConstants.UPDATE_CATEGORY_FORMAT00002.error_message
            ))
                    
        if errors:
            raise CustomValidationError(
                None,
                errors, 
                HTTPStatus.UNPROCESSABLE_ENTITY.value
            )   

        return errors
