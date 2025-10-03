from application.commons.queries import OrderingCriterionQuery
from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationErrorVm
from .search_products_by_object_ordering_dto import SearchProductsByObjectOrderingDto


class SearchProductsByObjectOrderingQuery(CustomValidator):

    def __init__(self, dto:SearchProductsByObjectOrderingDto):
        self.code = OrderingCriterionQuery(dto.code) if dto.code is not None else None
        self.name = OrderingCriterionQuery(dto.name) if dto.name is not None else None
        self.category = OrderingCriterionQuery(dto.category) if dto.category is not None else None
        self.description = OrderingCriterionQuery(dto.description) if dto.description is not None else None        
        self.created_at = OrderingCriterionQuery(dto.created_at) if dto.created_at is not None else None

    def format_validation(self):
        errors = []

        if self.code is not None and not self.code.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00001.error_code,
                property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00001.property_name,                    
                error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00001.error_message.format(
                    order_by=self.code.operator
                )
            ))

        if self.name is not None and not self.name.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00002.error_code,
                property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00002.property_name,                    
                error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00002.error_message.format(
                    order_by=self.name.operator
                )
            ))

        if self.category is not None and not self.category.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00003.error_code,
                property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00003.property_name,                    
                error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00003.error_message.format(
                    order_by=self.category.operator
                )
            ))

        if self.description is not None and not self.description.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00004.error_code,
                property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00004.property_name,                    
                error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00004.error_message.format(
                    order_by=self.description.operator
                )
            ))

        if self.created_at is not None and not self.created_at.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00005.error_code,
                property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00005.property_name,                    
                error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00005.error_message.format(
                    order_by=self.created_at.operator
                )
            ))

        return errors
