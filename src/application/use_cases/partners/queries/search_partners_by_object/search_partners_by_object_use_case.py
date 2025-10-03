import logging
from domain.query_objects import PartnersQuery, PartnersPaginatedQuery, PartnersQueryFilter, PartnersQueryOrder
from application.abstractions.persistence import PartnersRepositoryPort
from application.commons.queries import QueryBuilder
from application.commons.validators import validate_format_request_before
from application.commons.vms import PaginatedVm
from .search_partners_by_object_query import SearchPartnersByObjectQuery
from .search_partners_by_object_vm import SearchPartnersByObjectVm


logger = logging.getLogger(__name__)

class SearchPartnersByObjectUseCase:

    def __init__(self, partners_repository:PartnersRepositoryPort):
        self._partners_repository = partners_repository

    def _buildPartnerFilteringCriteria(self, query:SearchPartnersByObjectQuery):
        if query.filtering_criteria is None:
            return None

        return PartnersQueryFilter(
            code=QueryBuilder.filtering_builder(query.filtering_criteria.code),
            name=QueryBuilder.filtering_builder(query.filtering_criteria.name),
            contact=QueryBuilder.filtering_builder(query.filtering_criteria.contact),
            phone=QueryBuilder.filtering_builder(query.filtering_criteria.phone),
            address=QueryBuilder.filtering_builder(query.filtering_criteria.address),
            email=QueryBuilder.filtering_builder(query.filtering_criteria.email),
            created_at=QueryBuilder.filtering_builder(query.filtering_criteria.created_at)
        )

    def _buildPartnerOrderingCriteria(self, query:SearchPartnersByObjectQuery):
        if query.ordering_criteria is None:
            return None

        return PartnersQueryOrder(
            code=QueryBuilder.ordering_builder(query.ordering_criteria.code),
            name=QueryBuilder.ordering_builder(query.ordering_criteria.name),
            contact=QueryBuilder.ordering_builder(query.ordering_criteria.contact),
            phone=QueryBuilder.ordering_builder(query.ordering_criteria.phone),
            address=QueryBuilder.ordering_builder(query.ordering_criteria.address),
            email=QueryBuilder.ordering_builder(query.ordering_criteria.email),            
            created_at=QueryBuilder.ordering_builder(query.ordering_criteria.created_at)
        )

    @validate_format_request_before
    async def execute(self, query:SearchPartnersByObjectQuery):
        partner_filtering_criteria = self._buildPartnerFilteringCriteria(query)
        partner_ordering_criteria = self._buildPartnerOrderingCriteria(query)
        data_list = await self._partners_repository.search_partners_by_object_async(
            PartnersPaginatedQuery(
                filtering_criteria=partner_filtering_criteria,
                ordering_criteria=partner_ordering_criteria,
                current_page=query.current_page,
                page_size=query.page_size
            )
        )
        total_count = await self._partners_repository.total_count_partners_by_object_async(
            PartnersQuery(filtering_criteria=partner_filtering_criteria)
        )
        vm = PaginatedVm[SearchPartnersByObjectVm](
            [SearchPartnersByObjectVm.map_from_entities(data) for data in data_list],
            total_count,
            query.current_page,
            query.page_size
        )

        return vm.model_dump()