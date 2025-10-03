import logging
from application.abstractions.persistence import CategoriesRepositoryPort
from application.commons.vms import PaginatedVm
from application.commons.validators import validate_format_request_before
from .search_categories_by_text_query import SearchCategoriesByTextQuery
from .search_categories_by_text_vm import SearchCategoriesByTextVm


logger = logging.getLogger(__name__)

class SearchCategoriesByTextUseCase:
    
    def __init__(self, categories_repository:CategoriesRepositoryPort):
        self._categories_repository = categories_repository

    @validate_format_request_before
    async def execute(self, query:SearchCategoriesByTextQuery):
        data_list = await self._categories_repository.search_categories_by_text_async(
            query.text_filter, query.current_page, query.page_size
        )
        total_count = await self._categories_repository.total_count_categories_by_text_async(query.text_filter)        
        vm = PaginatedVm[SearchCategoriesByTextVm](
            [SearchCategoriesByTextVm.map_from_entities(data) for data in data_list], 
            total_count, 
            query.current_page, 
            query.page_size
        )
        
        return vm.model_dump()