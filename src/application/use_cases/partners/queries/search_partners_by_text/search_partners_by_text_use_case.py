import logging
from application.abstractions.persistence import PartnersRepositoryPort
from application.commons.vms import PaginatedVm
from application.commons.validators import validate_format_request_before
from .search_partners_by_text_query import SearchPartnersByTextQuery
from .search_partners_by_text_vm import SearchPartnersByTextVm


logger = logging.getLogger(__name__)

class SearchPartnersByTextUseCase:

    def __init__(self, partners_repository:PartnersRepositoryPort):
        self._partners_repository = partners_repository

    @validate_format_request_before
    async def execute(self, query:SearchPartnersByTextQuery):
        data_list = await self._partners_repository.search_partners_by_text_async(
            query.text_filter, query.current_page, query.page_size
        )
        total_count = await self._partners_repository.total_count_partners_by_text_async(query.text_filter)
        vm = PaginatedVm[SearchPartnersByTextVm](
            [SearchPartnersByTextVm.map_from_entities(data) for data in data_list],
            total_count,
            query.current_page,
            query.page_size
        )

        return vm.model_dump()