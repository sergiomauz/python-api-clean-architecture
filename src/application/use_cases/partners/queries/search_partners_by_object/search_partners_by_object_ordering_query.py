from application.commons.queries import OrderingCriterionQuery
from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationErrorVm
from .search_partners_by_object_ordering_dto import SearchPartnersByObjectOrderingDto


class SearchPartnersByObjectOrderingQuery(CustomValidator):

    def __init__(self, dto:SearchPartnersByObjectOrderingDto):
        self.code = OrderingCriterionQuery(dto.code) if dto.code is not None else None
        self.name = OrderingCriterionQuery(dto.name) if dto.name is not None else None
        self.contact = OrderingCriterionQuery(dto.contact) if dto.contact is not None else None
        self.phone = OrderingCriterionQuery(dto.phone) if dto.phone is not None else None
        self.address = OrderingCriterionQuery(dto.address) if dto.address is not None else None
        self.email = OrderingCriterionQuery(dto.email) if dto.email is not None else None
        self.created_at = OrderingCriterionQuery(dto.created_at) if dto.created_at is not None else None

    def format_validation(self):
        errors = []
        
        if self.name is not None and not self.name.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00001.error_code,
                property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00001.property_name,                    
                error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00001.error_message.format(
                    order_by=self.name.operator
                )
            ))

        if self.contact is not None and not self.contact.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00002.error_code,
                property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00002.property_name,                    
                error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00002.error_message.format(
                    order_by=self.contact.operator
                )
            ))

        if self.phone is not None and not self.phone.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00003.error_code,
                property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00003.property_name,                    
                error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00003.error_message.format(
                    order_by=self.phone.operator
                )
            ))

        if self.address is not None and not self.address.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00004.error_code,
                property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00004.property_name,                    
                error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00004.error_message.format(
                    order_by=self.address.operator
                )
            ))

        if self.email is not None and not self.email.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00005.error_code,
                property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00005.property_name,                    
                error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00005.error_message.format(
                    order_by=self.email.operator
                )
            ))

        if self.created_at is not None and not self.created_at.is_valid_ordering_operation():
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00006.error_code,
                property_name=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00006.property_name,                    
                error_message=ErrorConstants.SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00006.error_message.format(
                    order_by=self.created_at.operator
                )
            ))

        return errors