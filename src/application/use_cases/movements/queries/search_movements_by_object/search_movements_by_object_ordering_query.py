from application.commons.queries import OrderingCriterionQuery
from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationErrorVm
from .search_movements_by_object_ordering_dto import SearchMovementsByObjectOrderingDto


class SearchMovementsByObjectOrderingQuery(CustomValidator):

    def __init__(self, dto:SearchMovementsByObjectOrderingDto):
        self.partner = OrderingCriterionQuery(dto.partner) if dto.partner is not None else None
        self.product = OrderingCriterionQuery(dto.product) if dto.product is not None else None
        self.quantity = OrderingCriterionQuery(dto.quantity) if dto.quantity is not None else None
        self.movement_type = OrderingCriterionQuery(dto.movement_type) if dto.movement_type is not None else None
        self.movement_date = OrderingCriterionQuery(dto.movement_date) if dto.movement_date is not None else None
        self.created_at = OrderingCriterionQuery(dto.created_at) if dto.created_at is not None else None

    def format_validation(self):
        errors = []
        
        if self.partner is not None and not self.partner.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00001.error_code,
                property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00001.property_name,                    
                error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00001.error_message.format(
                    order_by=self.partner.operator
                )
            ))

        if self.product is not None and not self.product.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00002.error_code,
                property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00002.property_name,                    
                error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00002.error_message.format(
                    order_by=self.product.operator
                )
            ))

        if self.quantity is not None and not self.quantity.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00003.error_code,
                property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00003.property_name,                    
                error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00003.error_message.format(
                    order_by=self.quantity.operator
                )
            ))

        if self.movement_type is not None and not self.movement_type.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00004.error_code,
                property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00004.property_name,                    
                error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00004.error_message.format(
                    order_by=self.movement_type.operator
                )
            ))

        if self.movement_date is not None and not self.movement_date.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00005.error_code,
                property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00005.property_name,                    
                error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00005.error_message.format(
                    order_by=self.movement_date.operator
                )
            ))

        if self.created_at is not None and not self.created_at.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00006.error_code,
                property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00006.property_name,                    
                error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00006.error_message.format(
                    order_by=self.created_at.operator
                )
            ))

        return errors