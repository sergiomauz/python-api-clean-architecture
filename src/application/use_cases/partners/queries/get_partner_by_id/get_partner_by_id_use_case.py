import logging
from http import HTTPStatus
from application.abstractions.persistence import PartnersRepositoryPort
from application.commons.validators import validate_format_request_before
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .get_partner_by_id_query import GetPartnerByIdQuery
from .get_partner_by_id_vm import GetPartnerByIdVm


logger = logging.getLogger(__name__)

class GetPartnerByIdUseCase:

    def __init__(self, partners_repository:PartnersRepositoryPort):
        self._partners_repository = partners_repository

    @validate_format_request_before
    async def execute(self, query:GetPartnerByIdQuery):
        data = await self._partners_repository.get_by_id_async(query.id)
        if not data:
            raise CustomValidationError(
                None,
                [CustomValidationErrorVm(
                    error_code=ErrorConstants.GET_PARTNER_BY_ID_CONTENT00001.error_code,
                    property_name=ErrorConstants.GET_PARTNER_BY_ID_CONTENT00001.property_name,                    
                    error_message=ErrorConstants.GET_PARTNER_BY_ID_CONTENT00001.error_message
                )],
                HTTPStatus.NOT_FOUND.value
            )
        vm = GetPartnerByIdVm.map_from_entities(data)

        return vm.model_dump()
