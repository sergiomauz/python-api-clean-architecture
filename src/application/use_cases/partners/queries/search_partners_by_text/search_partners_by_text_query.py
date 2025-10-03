from http import HTTPStatus
from application.commons.queries import BasicSearchQuery
from application.exceptions.errors import CustomValidationError
from .search_partners_by_text_request_params import SearchPartnersByTextRequestParams


class SearchPartnersByTextQuery(BasicSearchQuery):

    def __init__(self, request_params:SearchPartnersByTextRequestParams):
        super().__init__(
            text_filter=request_params.text_filter,
            page_size=request_params.page_size,
            current_page=request_params.current_page
        )
 
    def format_validation(self):
        errors = super().format_validation()
        if errors:
            raise CustomValidationError(
                None,
                errors, 
                HTTPStatus.UNPROCESSABLE_ENTITY.value
            )     

        return errors