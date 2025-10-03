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
from .update_category_command import UpdateCategoryCommand
from .update_category_vm import UpdateCategoryVm


logger = logging.getLogger(__name__)

class UpdateCategoryUseCase:
    
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
    async def execute(self, command:UpdateCategoryCommand):
        existing_category = await self._categories_repository.get_by_id_async(command.id)
        if not existing_category:
            raise CustomValidationError(
                None,
                [CustomValidationErrorVm(
                    error_code=ErrorConstants.UPDATE_CATEGORY_CONTENT00001.error_code,
                    property_name=ErrorConstants.UPDATE_CATEGORY_CONTENT00001.property_name,                    
                    error_message=ErrorConstants.UPDATE_CATEGORY_CONTENT00001.error_message
                )],
                HTTPStatus.NOT_FOUND.value)
                                    
        if command.name:
            category_filtering_criteria = self._buildCategoryFilteringCriteria(command.name)        
            existing_categories = await self._categories_repository.search_categories_by_object_async(
                CategoriesPaginatedQuery(
                    filtering_criteria=category_filtering_criteria,
                )
            )
            if len(existing_categories) > 0 and existing_categories[0].id != command.id:
                raise CustomValidationError(
                    None,
                    [CustomValidationErrorVm(
                        error_code=ErrorConstants.UPDATE_CATEGORY_CONTENT00002.error_code,
                        property_name=ErrorConstants.UPDATE_CATEGORY_CONTENT00002.property_name,                    
                        error_message=ErrorConstants.UPDATE_CATEGORY_CONTENT00002.error_message
                    )],
                    HTTPStatus.CONFLICT.value)
            existing_category.name = command.name
            
        if command.description: 
            existing_category.description = command.description
                        
        await self._categories_repository.update_and_commit_async(
            Category(     
                id=existing_category.id,               
                name=existing_category.name,
                description=existing_category.description
            )
        )
        vm = UpdateCategoryVm.map_from_entities(existing_category)
                    
        return vm.model_dump()
