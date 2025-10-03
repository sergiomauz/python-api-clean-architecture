import logging
from domain.query_objects import CategoriesQuery, CategoriesPaginatedQuery, CategoriesQueryFilter, CategoriesQueryOrder
from application.abstractions.persistence import CategoriesRepositoryPort
from application.commons.queries import QueryBuilder
from application.commons.validators import validate_format_request_before
from application.commons.vms import PaginatedVm
from .search_categories_by_object_query import SearchCategoriesByObjectQuery
from .search_categories_by_object_vm import SearchCategoriesByObjectVm


logger = logging.getLogger(__name__)

class SearchCategoriesByObjectUseCase:
    
    def __init__(self, categories_repository:CategoriesRepositoryPort):
        self._categories_repository = categories_repository

    def _buildCategoryFilteringCriteria(self, query:SearchCategoriesByObjectQuery):
        if query.filtering_criteria is None:
            return None
        
        return CategoriesQueryFilter(
            name=QueryBuilder.filtering_builder(query.filtering_criteria.name),
            description=QueryBuilder.filtering_builder(query.filtering_criteria.description),
            created_at=QueryBuilder.filtering_builder(query.filtering_criteria.created_at)
        )

    def _buildCategoryOrderingCriteria(self, query:SearchCategoriesByObjectQuery):
        if query.ordering_criteria is None:
            return None
        
        return CategoriesQueryOrder(
            name=QueryBuilder.ordering_builder(query.ordering_criteria.name),
            description=QueryBuilder.ordering_builder(query.ordering_criteria.description),
            created_at=QueryBuilder.ordering_builder(query.ordering_criteria.created_at)
        )

    @validate_format_request_before
    async def execute(self, query:SearchCategoriesByObjectQuery):        
        category_filtering_criteria = self._buildCategoryFilteringCriteria(query)
        category_ordering_criteria = self._buildCategoryOrderingCriteria(query)
        data_list = await self._categories_repository.search_categories_by_object_async(
            CategoriesPaginatedQuery(
                filtering_criteria=category_filtering_criteria,
                ordering_criteria=category_ordering_criteria,
                current_page=query.current_page,
                page_size=query.page_size
            )
        )
        total_count = await self._categories_repository.total_count_categories_by_object_async(
            CategoriesQuery(filtering_criteria=category_filtering_criteria)
        )        
        vm = PaginatedVm[SearchCategoriesByObjectVm](
            [SearchCategoriesByObjectVm.map_from_entities(data) for data in data_list], 
            total_count, 
            query.current_page, 
            query.page_size
        )
        
        return vm.model_dump()