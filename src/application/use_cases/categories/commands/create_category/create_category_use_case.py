import logging
from http import HTTPStatus
from commons.enums import FilterOperator
from domain.entities import Category
from domain.query_objects import CategoriesQueryFilter, CategoriesPaginatedQuery
from domain.query_objects.utils import FilteringCriterion
from application.abstractions.persistence import CategoriesRepositoryPort
from application.commons.validators import validate_format_request_before
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .create_category_command import CreateCategoryCommand
from .create_category_vm import CreateCategoryVm


logger = logging.getLogger(__name__)

class CreateCategoryUseCase:

    def __init__(self, categories_repository:CategoriesRepositoryPort):
        self._categories_repository = categories_repository
        
    def _buildCategoryFilteringCriteria(self, name:str):
        return CategoriesQueryFilter(
            name=FilteringCriterion(
                operator=FilterOperator.EQUALS,
                operand=name
            )
        )        

    @validate_format_request_before
    async def execute(self, command:CreateCategoryCommand):
        category_filtering_criteria = self._buildCategoryFilteringCriteria(command.name)        
        existing_categories = await self._categories_repository.search_categories_by_object_async(
            CategoriesPaginatedQuery(
                filtering_criteria=category_filtering_criteria,
            )
        )
        if len(existing_categories) > 0:        
            raise CustomValidationError(
                None,
                [CustomValidationErrorVm(
                    error_code=ErrorConstants.CREATE_CATEGORY_CONTENT00001.error_code,
                    property_name=ErrorConstants.CREATE_CATEGORY_CONTENT00001.property_name,                    
                    error_message=ErrorConstants.CREATE_CATEGORY_CONTENT00001.error_message
                )],
                HTTPStatus.CONFLICT.value)
                
        created_category = await self._categories_repository.create_and_commit_async(
            Category(
                name=command.name,
                description=command.description
            )
        )        
        vm = CreateCategoryVm.map_from_entities(created_category)            
        
        return vm.model_dump()
