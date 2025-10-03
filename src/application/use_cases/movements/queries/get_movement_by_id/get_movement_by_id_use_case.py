import logging
from http import HTTPStatus
from application.abstractions.persistence import MovementsRepositoryPort, ProductsRepositoryPort, PartnersRepositoryPort
from application.commons.validators import validate_format_request_before
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .get_movement_by_id_query import GetMovementByIdQuery
from .get_movement_by_id_vm import GetMovementByIdVm


logger = logging.getLogger(__name__)

class GetMovementByIdUseCase:

    def __init__(self, movements_repository:MovementsRepositoryPort, 
                 products_repository:ProductsRepositoryPort, 
                 partners_repository:PartnersRepositoryPort):
        self._movements_repository = movements_repository
        self._products_repository = products_repository
        self._partners_repository = partners_repository

    @validate_format_request_before
    async def execute(self, query:GetMovementByIdQuery):
        data = await self._movements_repository.get_by_id_async(query.id)
        if not data:
            raise CustomValidationError(
                None,
                [CustomValidationErrorVm(
                    error_code=ErrorConstants.GET_MOVEMENT_BY_ID_CONTENT00001.error_code,
                    property_name=ErrorConstants.GET_MOVEMENT_BY_ID_CONTENT00001.property_name,                    
                    error_message=ErrorConstants.GET_MOVEMENT_BY_ID_CONTENT00001.error_message
                )],
                HTTPStatus.NOT_FOUND.value
            )
        data.product = await self._products_repository.get_by_id_async(data.product_id)
        data.partner = await self._partners_repository.get_by_id_async(data.partner_id)        
        vm = GetMovementByIdVm.map_from_entities(data)

        return vm.model_dump()
