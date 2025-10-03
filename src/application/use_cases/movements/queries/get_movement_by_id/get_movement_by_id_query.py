from http import HTTPStatus
from application.commons.queries import UuidQuery
from application.exceptions.errors import CustomValidationError
from .get_movement_by_id_route import GetMovementByIdRoute


class GetMovementByIdQuery(UuidQuery):

    def __init__(self, route:GetMovementByIdRoute):
        super().__init__(id=route.id)

    def format_validation(self):
        errors = super().format_validation()
        if errors:
            raise CustomValidationError(
                None,
                errors,
                HTTPStatus.UNPROCESSABLE_ENTITY.value
            )

        return errors
