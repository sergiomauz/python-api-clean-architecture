import logging
from http import HTTPStatus
from commons.utils import CustomParsers
from domain.entities import Movement
from application.abstractions.persistence import (
    MovementsRepositoryPort, ProductsRepositoryPort, PartnersRepositoryPort
)
from application.commons.validators import validate_format_request_before
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .create_movement_command import CreateMovementCommand
from .create_movement_vm import CreateMovementVm


logger = logging.getLogger(__name__)

class CreateMovementUseCase:

    def __init__(self, movements_repository:MovementsRepositoryPort, products_repository=ProductsRepositoryPort, partners_repository=PartnersRepositoryPort):
        self._movements_repository = movements_repository
        self._products_repository = products_repository
        self._partners_repository = partners_repository

    @validate_format_request_before
    async def execute(self, command:CreateMovementCommand):
        existing_product = await self._products_repository.get_by_id_async(command.product_id)
        if not existing_product:
            raise CustomValidationError(
                None,
                [CustomValidationErrorVm(
                    error_code=ErrorConstants.CREATE_MOVEMENT_CONTENT00001.error_code,
                    property_name=ErrorConstants.CREATE_MOVEMENT_CONTENT00001.property_name,                    
                    error_message=ErrorConstants.CREATE_MOVEMENT_CONTENT00001.error_message
                )],
                HTTPStatus.CONFLICT.value)
        
        existing_partner = await self._partners_repository.get_by_id_async(command.partner_id)
        if not existing_partner:
            raise CustomValidationError(
                None,
                [CustomValidationErrorVm(
                    error_code=ErrorConstants.CREATE_MOVEMENT_CONTENT00002.error_code,
                    property_name=ErrorConstants.CREATE_MOVEMENT_CONTENT00002.property_name,                    
                    error_message=ErrorConstants.CREATE_MOVEMENT_CONTENT00002.error_message
                )],
                HTTPStatus.CONFLICT.value)        
        
        created_movement = await self._movements_repository.create_and_commit_async(
            Movement(
                partner_id=command.partner_id,
                product_id=command.product_id,
                movement_date=CustomParsers.to_datetime(command.movement_date),
                quantity=command.quantity,
                movement_type=command.movement_type
            )
        )        
        vm = CreateMovementVm.map_from_entities(
            movement=created_movement,
            product=existing_product,
            partner=existing_partner)

        return vm.model_dump()
