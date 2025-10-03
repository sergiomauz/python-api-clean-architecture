from http import HTTPStatus
from application.commons.queries import IdsQuery
from application.exceptions.errors import CustomValidationError
from .delete_product_route import DeleteProductRoute
from .delete_products_dto import DeleteProductsDto


class DeleteProductsCommand(IdsQuery):

    def __init__(self, route:DeleteProductRoute, dto:DeleteProductsDto):
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