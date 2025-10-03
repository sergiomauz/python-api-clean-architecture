import logging
from domain.query_objects import ProductsQuery, ProductsPaginatedQuery, ProductsQueryFilter, ProductsQueryOrder
from application.abstractions.persistence import ProductsRepositoryPort
from application.commons.queries import QueryBuilder
from application.commons.validators import validate_format_request_before
from application.commons.vms import PaginatedVm
from .search_products_by_object_query import SearchProductsByObjectQuery
from .search_products_by_object_vm import SearchProductsByObjectVm


logger = logging.getLogger(__name__)

class SearchProductsByObjectUseCase:

    def __init__(self, products_repository:ProductsRepositoryPort):
        self._products_repository = products_repository

    def _buildProductFilteringCriteria(self, query:SearchProductsByObjectQuery):
        if query.filtering_criteria is None:
            return None

        return ProductsQueryFilter(
            code=QueryBuilder.filtering_builder(query.filtering_criteria.code),
            name=QueryBuilder.filtering_builder(query.filtering_criteria.name),
            category=QueryBuilder.filtering_builder(query.filtering_criteria.category),
            description=QueryBuilder.filtering_builder(query.filtering_criteria.description),
            created_at=QueryBuilder.filtering_builder(query.filtering_criteria.created_at)
        )

    def _buildProductOrderingCriteria(self, query:SearchProductsByObjectQuery):
        if query.ordering_criteria is None:
            return None

        return ProductsQueryOrder(
            code=QueryBuilder.ordering_builder(query.ordering_criteria.code),
            name=QueryBuilder.ordering_builder(query.ordering_criteria.name),
            category=QueryBuilder.ordering_builder(query.ordering_criteria.category),
            description=QueryBuilder.ordering_builder(query.ordering_criteria.description),            
            created_at=QueryBuilder.ordering_builder(query.ordering_criteria.created_at)
        )

    @validate_format_request_before
    async def execute(self, query:SearchProductsByObjectQuery):
        product_filtering_criteria = self._buildProductFilteringCriteria(query)
        product_ordering_criteria = self._buildProductOrderingCriteria(query)
        data_list = await self._products_repository.search_products_by_object_async(
            ProductsPaginatedQuery(
                filtering_criteria=product_filtering_criteria,
                ordering_criteria=product_ordering_criteria,
                current_page=query.current_page,
                page_size=query.page_size
            )
        )
        total_count = await self._products_repository.total_count_products_by_object_async(
            ProductsQuery(filtering_criteria=product_filtering_criteria)
        )
        vm = PaginatedVm[SearchProductsByObjectVm](
            [SearchProductsByObjectVm.map_from_entities(data) for data in data_list],
            total_count,
            query.current_page,
            query.page_size
        )

        return vm.model_dump()
