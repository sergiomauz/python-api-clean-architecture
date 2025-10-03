import logging
from application.abstractions.persistence import ProductsRepositoryPort
from application.commons.vms import PaginatedVm
from application.commons.validators import validate_format_request_before
from .search_products_by_text_query import SearchProductsByTextQuery
from .search_products_by_text_vm import SearchProductsByTextVm


logger = logging.getLogger(__name__)

class SearchProductsByTextUseCase:

    def __init__(self, products_repository:ProductsRepositoryPort):
        self._products_repository = products_repository

    @validate_format_request_before
    async def execute(self, query:SearchProductsByTextQuery):
        data_list = await self._products_repository.search_products_by_text_async(
            query.text_filter, query.current_page, query.page_size
        )
        total_count = await self._products_repository.total_count_products_by_text_async(query.text_filter)
        vm = PaginatedVm[SearchProductsByTextVm](
            [SearchProductsByTextVm.map_from_entities(data) for data in data_list],
            total_count,
            query.current_page,
            query.page_size
        )

        return vm.model_dump()