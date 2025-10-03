from commons.utils import CustomParsers
from application.commons.queries import FilteringCriterionQuery
from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationErrorVm
from .search_products_by_object_filtering_dto import SearchProductsByObjectFilteringDto


class SearchProductsByObjectFilteringQuery(CustomValidator):

    def __init__(self, dto:SearchProductsByObjectFilteringDto):
        self.code = FilteringCriterionQuery(dto.code) if dto.code is not None else None
        self.name = FilteringCriterionQuery(dto.name) if dto.name is not None else None
        self.category = FilteringCriterionQuery(dto.category) if dto.category is not None else None
        self.description = FilteringCriterionQuery(dto.description) if dto.description is not None else None
        self.created_at = FilteringCriterionQuery(dto.created_at) if dto.created_at is not None else None

    def format_validation(self):
        errors = []

        if self.code is not None:
            if not (self.code.operand is not None and 
                    (isinstance(self.code.operand, str) or
                    (isinstance(self.code.operand, list) and CustomParsers.are_same_type(self.code.operand)))):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00001.error_code,
                    property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00001.property_name,                    
                    error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00001.error_message
                ))
            elif self.code.is_valid_filtering_operation():                                
                if len(self.code.operand) == 0 or len(self.code.operand) > 75:
                    errors.append(CustomValidationErrorVm(
                        error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00002.error_code,
                        property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00002.property_name,                    
                        error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00002.error_message
                    ))
            else:
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00003.error_code,
                    property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00003.property_name,                    
                    error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00003.error_message.format(
                        operator=self.code.operator, operand=self.code.operand
                    )
                ))

        if self.name is not None:
            if not (self.name.operand is not None and 
                    (isinstance(self.name.operand, str) or
                    (isinstance(self.name.operand, list) and CustomParsers.are_same_type(self.name.operand)))):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00004.error_code,
                    property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00004.property_name,                    
                    error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00004.error_message
                ))
            elif self.name.is_valid_filtering_operation():                                
                if len(self.name.operand) == 0 or len(self.name.operand) > 75:
                    errors.append(CustomValidationErrorVm(
                        error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00005.error_code,
                        property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00005.property_name,                    
                        error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00005.error_message
                    ))
            else:
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00006.error_code,
                    property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00006.property_name,                    
                    error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00006.error_message.format(
                        operator=self.name.operator, operand=self.name.operand
                    )
                ))

        if self.category is not None:
            if not (self.category.operand is not None and 
                    (isinstance(self.category.operand, str) or
                    (isinstance(self.category.operand, list) and CustomParsers.are_same_type(self.category.operand)))):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00007.error_code,
                    property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00007.property_name,                    
                    error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00007.error_message
                ))
            elif self.category.is_valid_filtering_operation():                                
                if len(self.category.operand) == 0 or len(self.category.operand) > 75:
                    errors.append(CustomValidationErrorVm(
                        error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00008.error_code,
                        property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00008.property_name,                    
                        error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00008.error_message
                    ))
            else:
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00009.error_code,
                    property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00009.property_name,                    
                    error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00009.error_message.format(
                        operator=self.category.operator, operand=self.category.operand
                    )
                ))

        if self.description is not None:
            if not (self.description.operand is not None and 
                    (isinstance(self.description.operand, str) or
                    (isinstance(self.description.operand, list) and CustomParsers.are_same_type(self.description.operand)))):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00010.error_code,
                    property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00010.property_name,                    
                    error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00010.error_message
                ))
            elif self.description.is_valid_filtering_operation():                                
                if len(self.description.operand) == 0 or len(self.description.operand) > 75:
                    errors.append(CustomValidationErrorVm(
                        error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00011.error_code,
                        property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00011.property_name,                    
                        error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00011.error_message
                    ))
            else:
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00012.error_code,
                    property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00012.property_name,                    
                    error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00012.error_message.format(
                        operator=self.description.operator, operand=self.description.operand
                    )
                ))

        if self.created_at is not None:
            if not (self.created_at.operand is not None and 
                    CustomParsers.are_valid_datetimes(self.created_at.operand)):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00013.error_code,
                    property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00013.property_name,                    
                    error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00013.error_message
                ))            
            elif not self.created_at.is_valid_filtering_operation():
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00014.error_code,
                    property_name=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00014.property_name,                    
                    error_message=ErrorConstants.SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00014.error_message.format(
                        operator=self.created_at.operator, operand=self.created_at.operand
                    )
                ))                                                        

        return errors
