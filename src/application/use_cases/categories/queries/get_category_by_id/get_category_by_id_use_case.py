import logging
from http import HTTPStatus
from application.abstractions.persistence import CategoriesRepositoryPort
from application.commons.validators import validate_format_request_before
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .get_category_by_id_query import GetCategoryByIdQuery
from .get_category_by_id_vm import GetCategoryByIdVm


logger = logging.getLogger(__name__)

class GetCategoryByIdUseCase:
    
    def __init__(self, categories_repository:CategoriesRepositoryPort):
        self._categories_repository = categories_repository

    @validate_format_request_before
    async def execute(self, query:GetCategoryByIdQuery):
        data = await self._categories_repository.get_by_id_async(query.id)
        if not data:
            raise CustomValidationError(
                None,
                [CustomValidationErrorVm(
                    error_code=ErrorConstants.GET_CATEGORY_BY_ID_CONTENT00001.error_code,
                    property_name=ErrorConstants.GET_CATEGORY_BY_ID_CONTENT00001.property_name,                    
                    error_message=ErrorConstants.GET_CATEGORY_BY_ID_CONTENT00001.error_message
                )],
                HTTPStatus.NOT_FOUND.value
            )
        vm = GetCategoryByIdVm.map_from_entities(data)
        
        return vm.model_dump()          
