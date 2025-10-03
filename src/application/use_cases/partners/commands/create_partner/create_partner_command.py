import re
from http import HTTPStatus
from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .create_partner_dto import CreatePartnerDto


class CreatePartnerCommand(CustomValidator):

    def __init__(self, dto:CreatePartnerDto):
        self.code = dto.code
        self.name = dto.name
        self.contact = dto.contact
        self.phone = dto.phone
        self.address = dto.address
        self.email = dto.email        

    def format_validation(self):
        errors = []
        if not self.code or (len(self.code) != 10):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_PARTNER_FORMAT00001.error_code,
                property_name=ErrorConstants.CREATE_PARTNER_FORMAT00001.property_name,                    
                error_message=ErrorConstants.CREATE_PARTNER_FORMAT00001.error_message
            ))        
        if not self.name or (len(self.name) < 5 or len(self.name) > 350):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_PARTNER_FORMAT00002.error_code,
                property_name=ErrorConstants.CREATE_PARTNER_FORMAT00002.property_name,                    
                error_message=ErrorConstants.CREATE_PARTNER_FORMAT00002.error_message
            ))
        if not self.contact or (len(self.contact) < 3 or len(self.contact) > 200):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_PARTNER_FORMAT00003.error_code,
                property_name=ErrorConstants.CREATE_PARTNER_FORMAT00003.property_name,                    
                error_message=ErrorConstants.CREATE_PARTNER_FORMAT00003.error_message
            ))
        if not self.phone or (len(self.phone) < 5 or len(self.phone) > 15 or not re.fullmatch(r"^\d+(?:-\d+)*$", self.phone)):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_PARTNER_FORMAT00004.error_code,
                property_name=ErrorConstants.CREATE_PARTNER_FORMAT00004.property_name,                    
                error_message=ErrorConstants.CREATE_PARTNER_FORMAT00004.error_message
            ))
        if not self.address or (len(self.address) < 5 or len(self.address) > 500):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_PARTNER_FORMAT00005.error_code,
                property_name=ErrorConstants.CREATE_PARTNER_FORMAT00005.property_name,                    
                error_message=ErrorConstants.CREATE_PARTNER_FORMAT00005.error_message
            ))
        if not self.email or (len(self.email) < 5 or len(self.email) > 100 or not re.fullmatch(r"^[\w\.-]+@[\w\.-]+\.\w+$", self.email)):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_PARTNER_FORMAT00006.error_code,
                property_name=ErrorConstants.CREATE_PARTNER_FORMAT00006.property_name,                    
                error_message=ErrorConstants.CREATE_PARTNER_FORMAT00006.error_message
            ))

        if errors:
            raise CustomValidationError(
                None,
                errors,
                HTTPStatus.UNPROCESSABLE_ENTITY.value
            )

        return errors
