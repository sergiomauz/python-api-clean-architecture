from commons.enums import MovementType
from commons.utils import CustomParsers
from application.commons.queries import FilteringCriterionQuery
from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationErrorVm
from .search_movements_by_object_filtering_dto import SearchMovementsByObjectFilteringDto


class SearchMovementsByObjectFilteringQuery(CustomValidator):

    def __init__(self, dto:SearchMovementsByObjectFilteringDto):
        self.partner = FilteringCriterionQuery(dto.partner) if dto.partner is not None else None
        self.product = FilteringCriterionQuery(dto.product) if dto.product is not None else None
        self.quantity = FilteringCriterionQuery(dto.quantity) if dto.quantity is not None else None
        self.movement_type = FilteringCriterionQuery(dto.movement_type) if dto.movement_type is not None else None
        self.movement_date = FilteringCriterionQuery(dto.movement_date) if dto.movement_date is not None else None
        self.created_at = FilteringCriterionQuery(dto.created_at) if dto.created_at is not None else None

    def format_validation(self):
        errors = []

        if self.partner is not None:
            if not (self.partner.operand is not None and 
                    (isinstance(self.partner.operand, str) or
                    (isinstance(self.partner.operand, list) and CustomParsers.are_same_type(self.partner.operand)))):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00001.error_code,
                    property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00001.property_name,                    
                    error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00001.error_message
                ))
            elif self.partner.is_valid_filtering_operation():                                
                if len(self.partner.operand) == 0 or len(self.partner.operand) > 75:
                    errors.append(CustomValidationErrorVm(
                        error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00002.error_code,
                        property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00002.property_name,                    
                        error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00002.error_message
                    ))
            else:
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00003.error_code,
                    property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00003.property_name,                    
                    error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00003.error_message.format(
                        operator=self.partner.operator, operand=self.partner.operand
                    )
                ))

        if self.product is not None:
            if not (self.product.operand is not None and 
                    (isinstance(self.product.operand, str) or
                    (isinstance(self.product.operand, list) and CustomParsers.are_same_type(self.product.operand)))):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00004.error_code,
                    property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00004.property_name,                    
                    error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00004.error_message
                ))
            elif self.product.is_valid_filtering_operation():                                
                if len(self.product.operand) == 0 or len(self.product.operand) > 75:
                    errors.append(CustomValidationErrorVm(
                        error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00005.error_code,
                        property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00005.property_name,                    
                        error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00005.error_message
                    ))
            else:
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00006.error_code,
                    property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00006.property_name,                    
                    error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00006.error_message.format(
                        operator=self.product.operator, operand=self.product.operand
                    )
                ))

        if self.quantity is not None:
            if not (self.quantity.operand is not None and 
                    (isinstance(self.quantity.operand, (int, float)) or
                    (isinstance(self.quantity.operand, list) and CustomParsers.are_same_type(self.quantity.operand)))):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00007.error_code,
                    property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00007.property_name,                    
                    error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00007.error_message
                ))
            elif self.quantity.is_valid_filtering_operation():                                
                if self.quantity.operand < 0:
                    errors.append(CustomValidationErrorVm(
                        error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00008.error_code,
                        property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00008.property_name,                    
                        error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00008.error_message
                    ))
            else:
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00009.error_code,
                    property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00009.property_name,                    
                    error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00009.error_message.format(
                        operator=self.quantity.operator, operand=self.quantity.operand
                    )
                ))

        if self.movement_type is not None:
            if not (self.movement_type.operand is not None and 
                    (isinstance(self.movement_type.operand, str) or
                    (isinstance(self.movement_type.operand, list) and CustomParsers.are_same_type(self.movement_type.operand)))):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00010.error_code,
                    property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00010.property_name,                    
                    error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00010.error_message
                ))
            elif self.movement_type.is_valid_filtering_operation():                                
                if MovementType.from_value(self.movement_type.operand) is None:
                    errors.append(CustomValidationErrorVm(
                        error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00011.error_code,
                        property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00011.property_name,                    
                        error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00011.error_message
                    ))
            else:
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00012.error_code,
                    property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00012.property_name,
                    error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00012.error_message.format(
                        operator=self.movement_type.operator, operand=self.movement_type.operand
                    )
                ))

        if self.movement_date is not None:
            if not (self.movement_date.operand is not None and 
                    CustomParsers.are_valid_datetimes(self.movement_date.operand)):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00013.error_code,
                    property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00013.property_name,                    
                    error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00013.error_message
                ))            
            elif not self.movement_date.is_valid_filtering_operation():
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00014.error_code,
                    property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00014.property_name,                    
                    error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00014.error_message.format(
                        operator=self.movement_date.operator, operand=self.movement_date.operand
                    )
                ))

        if self.created_at is not None:
            if not (self.created_at.operand is not None and 
                    CustomParsers.are_valid_datetimes(self.created_at.operand)):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00015.error_code,
                    property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00015.property_name,                    
                    error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00015.error_message
                ))            
            elif not self.created_at.is_valid_filtering_operation():
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00016.error_code,
                    property_name=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00016.property_name,                    
                    error_message=ErrorConstants.SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00016.error_message.format(
                        operator=self.created_at.operator, operand=self.created_at.operand
                    )
                ))

        return errors
