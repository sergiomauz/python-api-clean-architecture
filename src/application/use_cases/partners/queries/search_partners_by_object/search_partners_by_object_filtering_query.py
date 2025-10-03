from commons.utils import CustomParsers
from application.commons.queries import FilteringCriterionQuery
from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationErrorVm
from .search_partners_by_object_filtering_dto import SearchPartnersByObjectFilteringDto


class SearchPartnersByObjectFilteringQuery(CustomValidator):

    def __init__(self, dto:SearchPartnersByObjectFilteringDto):
        self.code = FilteringCriterionQuery(dto.code) if dto.code is not None else None
        self.name = FilteringCriterionQuery(dto.name) if dto.name is not None else None
        self.contact = FilteringCriterionQuery(dto.contact) if dto.contact is not None else None
        self.phone = FilteringCriterionQuery(dto.phone) if dto.phone is not None else None
        self.address = FilteringCriterionQuery(dto.address) if dto.address is not None else None
        self.email = FilteringCriterionQuery(dto.email) if dto.email is not None else None
        self.created_at = FilteringCriterionQuery(dto.created_at) if dto.created_at is not None else None

    def format_validation(self):
        errors = []

        if self.code is not None:
            if not (self.code.operand is not None and 
                    (isinstance(self.code.operand, str) or
                    (isinstance(self.code.operand, list) and CustomParsers.are_same_type(self.code.operand)))):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00001.error_code,
                    property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00001.property_name,                    
                    error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00001.error_message
                ))
            elif self.code.is_valid_filtering_operation():                                
                if len(self.code.operand) == 0 or len(self.code.operand) > 15:
                    errors.append(CustomValidationErrorVm(
                        error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00002.error_code,
                        property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00002.property_name,                    
                        error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00002.error_message
                    ))
            else:
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00003.error_code,
                    property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00003.property_name,                    
                    error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00003.error_message.format(
                        operator=self.code.operator, operand=self.code.operand
                    )
                ))

        if self.name is not None:
            if not (self.name.operand is not None and 
                    (isinstance(self.name.operand, str) or
                    (isinstance(self.name.operand, list) and CustomParsers.are_same_type(self.name.operand)))):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00004.error_code,
                    property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00004.property_name,                    
                    error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00004.error_message
                ))
            elif self.name.is_valid_filtering_operation():                                
                if len(self.name.operand) == 0 or len(self.name.operand) > 75:
                    errors.append(CustomValidationErrorVm(
                        error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00005.error_code,
                        property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00005.property_name,                    
                        error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00005.error_message
                    ))
            else:
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00006.error_code,
                    property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00006.property_name,                    
                    error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00006.error_message.format(
                        operator=self.name.operator, operand=self.name.operand
                    )
                ))

        if self.contact is not None:
            if not (self.contact.operand is not None and 
                    (isinstance(self.contact.operand, str) or
                    (isinstance(self.contact.operand, list) and CustomParsers.are_same_type(self.contact.operand)))):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00007.error_code,
                    property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00007.property_name,                    
                    error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00007.error_message
                ))
            elif self.contact.is_valid_filtering_operation():                                
                if len(self.contact.operand) == 0 or len(self.contact.operand) > 75:
                    errors.append(CustomValidationErrorVm(
                        error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00008.error_code,
                        property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00008.property_name,                    
                        error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00008.error_message
                    ))
            else:
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00009.error_code,
                    property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00009.property_name,                    
                    error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00009.error_message.format(
                        operator=self.contact.operator, operand=self.contact.operand
                    )
                ))

        if self.phone is not None:
            if not (self.phone.operand is not None and 
                    (isinstance(self.phone.operand, str) or
                    (isinstance(self.phone.operand, list) and CustomParsers.are_same_type(self.phone.operand)))):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00010.error_code,
                    property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00010.property_name,                    
                    error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00010.error_message
                ))
            elif self.phone.is_valid_filtering_operation():                                
                if len(self.phone.operand) == 0 or len(self.phone.operand) > 15:
                    errors.append(CustomValidationErrorVm(
                        error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00011.error_code,
                        property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00011.property_name,                    
                        error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00011.error_message
                    ))
            else:
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00012.error_code,
                    property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00012.property_name,                    
                    error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00012.error_message.format(
                        operator=self.phone.operator, operand=self.phone.operand
                    )
                ))

        if self.address is not None:
            if not (self.address.operand is not None and 
                    (isinstance(self.address.operand, str) or
                    (isinstance(self.address.operand, list) and CustomParsers.are_same_type(self.address.operand)))):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00013.error_code,
                    property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00013.property_name,                    
                    error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00013.error_message
                ))
            elif self.address.is_valid_filtering_operation():                                
                if len(self.address.operand) == 0 or len(self.address.operand) > 75:
                    errors.append(CustomValidationErrorVm(
                        error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00014.error_code,
                        property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00014.property_name,                    
                        error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00014.error_message
                    ))
            else:
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00015.error_code,
                    property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00015.property_name,                    
                    error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00015.error_message.format(
                        operator=self.address.operator, operand=self.address.operand
                    )
                ))

        if self.email is not None:
            if not (self.email.operand is not None and 
                    (isinstance(self.email.operand, str) or
                    (isinstance(self.email.operand, list) and CustomParsers.are_same_type(self.email.operand)))):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00016.error_code,
                    property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00016.property_name,                    
                    error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00016.error_message
                ))
            elif self.email.is_valid_filtering_operation():                                
                if len(self.email.operand) == 0 or len(self.email.operand) > 75:
                    errors.append(CustomValidationErrorVm(
                        error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00017.error_code,
                        property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00017.property_name,                    
                        error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00017.error_message
                    ))
            else:
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00018.error_code,
                    property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00018.property_name,                    
                    error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00018.error_message.format(
                        operator=self.email.operator, operand=self.email.operand
                    )
                ))                                                                

        if self.created_at is not None:
            if not (self.created_at.operand is not None and 
                    CustomParsers.are_valid_datetimes(self.created_at.operand)):
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00019.error_code,
                    property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00019.property_name,                    
                    error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00019.error_message
                ))            
            elif not self.created_at.is_valid_filtering_operation():
                errors.append(CustomValidationErrorVm(
                    error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00020.error_code,
                    property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00020.property_name,                    
                    error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00020.error_message.format(
                        operator=self.created_at.operator, operand=self.created_at.operand
                    )
                ))

        return errors
