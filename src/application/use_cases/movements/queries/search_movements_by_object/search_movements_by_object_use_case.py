import logging
from domain.query_objects import MovementsQuery, MovementsPaginatedQuery, MovementsQueryFilter, MovementsQueryOrder
from application.abstractions.persistence import MovementsRepositoryPort
from application.commons.queries import QueryBuilder
from application.commons.validators import validate_format_request_before
from application.commons.vms import PaginatedVm
from .search_movements_by_object_query import SearchMovementsByObjectQuery
from .search_movements_by_object_vm import SearchMovementsByObjectVm


logger = logging.getLogger(__name__)

class SearchMovementsByObjectUseCase:

    def __init__(self, movements_repository:MovementsRepositoryPort):
        self._movements_repository = movements_repository

    def _buildMovementFilteringCriteria(self, query:SearchMovementsByObjectQuery):
        if query.filtering_criteria is None:
            return None

        return MovementsQueryFilter(
            partner=QueryBuilder.filtering_builder(query.filtering_criteria.partner),
            product=QueryBuilder.filtering_builder(query.filtering_criteria.product),
            quantity=QueryBuilder.filtering_builder(query.filtering_criteria.quantity),
            movement_type=QueryBuilder.filtering_builder(query.filtering_criteria.movement_type),
            movement_date=QueryBuilder.filtering_builder(query.filtering_criteria.movement_date),
            created_at=QueryBuilder.filtering_builder(query.filtering_criteria.created_at)
        )

    def _buildMovementOrderingCriteria(self, query:SearchMovementsByObjectQuery):
        if query.ordering_criteria is None:
            return None

        return MovementsQueryOrder(
            partner=QueryBuilder.ordering_builder(query.ordering_criteria.partner),
            product=QueryBuilder.ordering_builder(query.ordering_criteria.product),
            quantity=QueryBuilder.ordering_builder(query.ordering_criteria.quantity),
            movement_type=QueryBuilder.ordering_builder(query.ordering_criteria.movement_type),
            movement_date=QueryBuilder.ordering_builder(query.ordering_criteria.movement_date),            
            created_at=QueryBuilder.ordering_builder(query.ordering_criteria.created_at)
        )

    @validate_format_request_before
    async def execute(self, query:SearchMovementsByObjectQuery):
        movement_filtering_criteria = self._buildMovementFilteringCriteria(query)
        movement_ordering_criteria = self._buildMovementOrderingCriteria(query)
        data_list = await self._movements_repository.search_movements_by_object_async(
            MovementsPaginatedQuery(
                filtering_criteria=movement_filtering_criteria,
                ordering_criteria=movement_ordering_criteria,
                current_page=query.current_page,
                page_size=query.page_size
            )
        )
        total_count = await self._movements_repository.total_count_movements_by_object_async(
            MovementsQuery(filtering_criteria=movement_filtering_criteria)
        )
        vm = PaginatedVm[SearchMovementsByObjectVm](
            [SearchMovementsByObjectVm.map_from_entities(data) for data in data_list],
            total_count,
            query.current_page,
            query.page_size
        )

        return vm.model_dump()