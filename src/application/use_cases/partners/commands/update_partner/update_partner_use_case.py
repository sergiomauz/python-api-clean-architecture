import logging
from http import HTTPStatus
from domain.entities import Partner
from application.abstractions.persistence import PartnersRepositoryPort
from application.commons.validators import validate_format_request_before
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .update_partner_command import UpdatePartnerCommand
from .update_partner_vm import UpdatePartnerVm


logger = logging.getLogger(__name__)

class UpdatePartnerUseCase:

    def __init__(self, partners_repository:PartnersRepositoryPort):
        self._partners_repository = partners_repository

    @validate_format_request_before
    async def execute(self, command:UpdatePartnerCommand):
        existing_partner = await self._partners_repository.get_by_id_async(command.id)
        if not existing_partner:
            raise CustomValidationError(
                None,
                [CustomValidationErrorVm(
                    error_code=ErrorConstants.UPDATE_PARTNER_CONTENT00001.error_code,
                    property_name=ErrorConstants.UPDATE_PARTNER_CONTENT00001.property_name,                    
                    error_message=ErrorConstants.UPDATE_PARTNER_CONTENT00001.error_message
                )],
                HTTPStatus.NOT_FOUND.value)
                
        if command.code:
            existing_partner_by_code = await self._partners_repository.get_by_code_async(command.code)
            if existing_partner_by_code and command.id != existing_partner_by_code.id:
                raise CustomValidationError(
                    None,
                    [CustomValidationErrorVm(
                        error_code=ErrorConstants.UPDATE_PARTNER_CONTENT00002.error_code,
                        property_name=ErrorConstants.UPDATE_PARTNER_CONTENT00002.property_name,                    
                        error_message=ErrorConstants.UPDATE_PARTNER_CONTENT00002.error_message
                    )],
                    HTTPStatus.CONFLICT.value)
            existing_partner.code = command.code
                
        if command.name: 
            existing_partner.name = command.name
                    
        if command.contact: 
            existing_partner.contact = command.contact
            
        if command.phone: 
            existing_partner.phone = command.phone
            
        if command.address: 
            existing_partner.address = command.address
            
        if command.email: 
            existing_partner.email = command.email
                                                                    
        await self._partners_repository.update_and_commit_async(
            Partner(
                id=existing_partner.id,
                code=existing_partner.code,
                name=existing_partner.name,
                contact=existing_partner.contact,
                phone=existing_partner.phone,
                address=existing_partner.address,
                email=existing_partner.email                
            )
        )
        vm = UpdatePartnerVm.map_from_entities(existing_partner)

        return vm.model_dump()
