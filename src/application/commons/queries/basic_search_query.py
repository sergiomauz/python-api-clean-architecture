from application.exceptions.errors import CustomValidationErrorVm
from application.error_catalog import ErrorConstants
from .paginated_query import PaginatedQuery


class BasicSearchQuery(PaginatedQuery):

    def __init__(self, text_filter:str, page_size:int, current_page:int):
        super().__init__(
            page_size=page_size,
            current_page=current_page            
        )
        self.text_filter = text_filter

    def format_validation(self):
        errors = super().format_validation()        
        if not self.text_filter or len(self.text_filter) > 75:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.BASIC_SEARCH_FORMAT00001.error_code,
                property_name=ErrorConstants.BASIC_SEARCH_FORMAT00001.property_name,                    
                error_message=ErrorConstants.BASIC_SEARCH_FORMAT00001.error_message
            ))        

        return errors
