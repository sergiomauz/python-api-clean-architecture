import logging
from application.abstractions.persistence import MovementsRepositoryPort
from application.commons.vms import PaginatedVm
from application.commons.validators import validate_format_request_before
from .search_movements_by_text_query import SearchMovementsByTextQuery
from .search_movements_by_text_vm import SearchMovementsByTextVm


logger = logging.getLogger(__name__)

class SearchMovementsByTextUseCase:

    def __init__(self, movements_repository:MovementsRepositoryPort):
        self._movements_repository = movements_repository

    @validate_format_request_before
    async def execute(self, query:SearchMovementsByTextQuery):
        data_list = await self._movements_repository.search_movements_by_text_async(
            query.text_filter, query.current_page, query.page_size
        )
        total_count = await self._movements_repository.total_count_movements_by_text_async(query.text_filter)
        vm = PaginatedVm[SearchMovementsByTextVm](
            [SearchMovementsByTextVm.map_from_entities(data) for data in data_list],
            total_count,
            query.current_page,
            query.page_size
        )

        return vm.model_dump()