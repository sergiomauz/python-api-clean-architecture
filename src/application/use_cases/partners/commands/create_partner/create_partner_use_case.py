import logging
from http import HTTPStatus
from domain.entities import Partner
from application.abstractions.persistence import PartnersRepositoryPort
from application.commons.validators import validate_format_request_before
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .create_partner_command import CreatePartnerCommand
from .create_partner_vm import CreatePartnerVm


logger = logging.getLogger(__name__)

class CreatePartnerUseCase:

    def __init__(self, partners_repository:PartnersRepositoryPort):
        self._partners_repository = partners_repository

    @validate_format_request_before
    async def execute(self, command:CreatePartnerCommand):
        existing_partner = await self._partners_repository.get_by_code_async(command.code)
        if existing_partner:
            raise CustomValidationError(
                None,
                [CustomValidationErrorVm(
                    error_code=ErrorConstants.CREATE_PARTNER_CONTENT00001.error_code,
                    property_name=ErrorConstants.CREATE_PARTNER_CONTENT00001.property_name,                    
                    error_message=ErrorConstants.CREATE_PARTNER_CONTENT00001.error_message
                )],
                HTTPStatus.CONFLICT.value)

        created_partner = await self._partners_repository.create_and_commit_async(
            Partner(
                code=command.code,
                name=command.name,
                contact=command.contact,
                phone=command.phone,
                address=command.address,
                email=command.email
            )
        )
        vm = CreatePartnerVm.map_from_entities(created_partner)

        return vm.model_dump()
