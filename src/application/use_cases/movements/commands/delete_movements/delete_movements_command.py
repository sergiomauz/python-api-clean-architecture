from http import HTTPStatus
from application.commons.queries import UuidsQuery
from application.exceptions.errors import CustomValidationError
from .delete_movement_route import DeleteMovementRoute
from .delete_movements_dto import DeleteMovementsDto


class DeleteMovementsCommand(UuidsQuery):

    def __init__(self, route:DeleteMovementRoute, dto:DeleteMovementsDto):
        if route and route.id:
            super().__init__(ids=[route.id])
        elif dto and dto.ids and len(dto.ids) > 0:
            super().__init__(ids=dto.ids)

    def format_validation(self):
        errors = super().format_validation()
        if errors:
            raise CustomValidationError(
                None,
                errors, 
                HTTPStatus.UNPROCESSABLE_ENTITY.value)   

        return errors