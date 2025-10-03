from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationErrorVm


class PaginatedQuery(CustomValidator):

    def __init__(self, page_size:int, current_page:int):
        self.page_size = page_size or 20
        self.current_page = current_page or 1
        
    def format_validation(self):
        errors = []
        if self.page_size < 1 or self.page_size > 300:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.PAGINATED_FORMAT00001.error_code,
                property_name=ErrorConstants.PAGINATED_FORMAT00001.property_name,                    
                error_message=ErrorConstants.PAGINATED_FORMAT00001.error_message
            ))
        if self.current_page < 1:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.PAGINATED_FORMAT00002.error_code,
                property_name=ErrorConstants.PAGINATED_FORMAT00002.property_name,                    
                error_message=ErrorConstants.PAGINATED_FORMAT00002.error_message
            ))        

        return errors 