from http import HTTPStatus
from application.commons.queries import IdQuery
from application.exceptions.errors import CustomValidationError
from .get_category_by_id_route import GetCategoryByIdRoute


class GetCategoryByIdQuery(IdQuery):

    def __init__(self, route:GetCategoryByIdRoute):
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
