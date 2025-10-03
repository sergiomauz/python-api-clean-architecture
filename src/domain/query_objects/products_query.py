from typing import Optional
from commons.enums import OrderOperator
from domain.query_objects.utils import FilteringCriterion, QueryTemplate, PaginatedQueryTemplate


class ProductsQueryFilter:
    def __init__(self, 
                name:Optional[FilteringCriterion]=None, 
                code:Optional[FilteringCriterion]=None, 
                category:Optional[FilteringCriterion]=None,
                description:Optional[FilteringCriterion]=None, 
                created_at:Optional[FilteringCriterion]=None):
        self.name = name
        self.code = code
        self.category = category
        self.description = description
        self.created_at = created_at
        

class ProductsQueryOrder:
    def __init__(self, 
                name:Optional[OrderOperator]=None, 
                code:Optional[OrderOperator]=None,
                category:Optional[OrderOperator]=None,
                description:Optional[OrderOperator]=None, 
                created_at:Optional[OrderOperator]=None):
        self.name = name
        self.code = code
        self.category = category
        self.description = description
        self.created_at = created_at


class ProductsQuery(QueryTemplate[ProductsQueryFilter, ProductsQueryOrder]):
    pass


class ProductsPaginatedQuery(PaginatedQueryTemplate[ProductsQueryFilter, ProductsQueryOrder]):
    pass