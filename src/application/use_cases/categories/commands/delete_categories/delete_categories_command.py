from http import HTTPStatus
from application.commons.queries import IdsQuery
from application.exceptions.errors import CustomValidationError
from .delete_category_route import DeleteCategoryRoute
from .delete_categories_dto import DeleteCategoriesDto


class DeleteCategoriesCommand(IdsQuery):
   
    def __init__(self, route:DeleteCategoryRoute, dto:DeleteCategoriesDto):
        if route and route.id:        
            super().__init__([route.id])
        elif dto and dto.ids and len(dto.ids) > 0:
            super().__init__(dto.ids)
            
    def format_validation(self):        
        errors = super().format_validation()
        if errors:
            raise CustomValidationError(
                None,
                errors, 
                HTTPStatus.UNPROCESSABLE_ENTITY.value
            )   

        return errors        