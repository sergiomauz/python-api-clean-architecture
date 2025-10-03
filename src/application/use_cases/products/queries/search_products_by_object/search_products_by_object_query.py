from http import HTTPStatus
from application.commons.queries import PaginatedQuery
from application.exceptions.errors import CustomValidationError
from .search_products_by_object_dto import SearchProductsByObjectDto
from .search_products_by_object_filtering_query import SearchProductsByObjectFilteringQuery
from .search_products_by_object_ordering_query import SearchProductsByObjectOrderingQuery


class SearchProductsByObjectQuery(PaginatedQuery):

    def __init__(self, dto:SearchProductsByObjectDto):
        super().__init__(
            current_page=dto.current_page,
            page_size=dto.page_size
        )
        self.filtering_criteria = SearchProductsByObjectFilteringQuery(dto.filtering_criteria) if dto.filtering_criteria is not None else None
        self.ordering_criteria = SearchProductsByObjectOrderingQuery(dto.ordering_criteria) if dto.ordering_criteria is not None else None

    def format_validation(self):
        errors = []
        
        paginated_errors = super().format_validation()
        if len(paginated_errors) > 0:
            errors.extend(paginated_errors)

        if self.filtering_criteria is not None:
            filtering_criteria_errors = self.filtering_criteria.format_validation()        
            if len(filtering_criteria_errors) > 0:
                errors.extend(filtering_criteria_errors)

        if self.ordering_criteria is not None:
            ordering_criteria_errors = self.ordering_criteria.format_validation()
            if len(ordering_criteria_errors) > 0:
                errors.extend(ordering_criteria_errors)        
        
        if errors:
            raise CustomValidationError(
                None,
                errors, 
                HTTPStatus.UNPROCESSABLE_ENTITY.value
            )
            
        return errors
