from http import HTTPStatus
from application.commons.queries import IdQuery
from application.exceptions.errors import CustomValidationError
from .get_product_by_id_route import GetProductByIdRoute


class GetProductByIdQuery(IdQuery):

    def __init__(self, route:GetProductByIdRoute):
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
