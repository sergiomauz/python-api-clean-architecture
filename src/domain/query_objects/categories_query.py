from typing import Optional
from commons.enums import OrderOperator
from domain.query_objects.utils import FilteringCriterion, QueryTemplate, PaginatedQueryTemplate


class CategoriesQueryFilter:
    def __init__(self, 
                 name:Optional[FilteringCriterion]=None, 
                 description:Optional[FilteringCriterion]=None, 
                 created_at:Optional[FilteringCriterion]=None):
        self.name = name
        self.description = description
        self.created_at = created_at
        

class CategoriesQueryOrder:
    def __init__(self, 
                 name:Optional[OrderOperator]=None, 
                 description:Optional[OrderOperator]=None, 
                 created_at:Optional[OrderOperator]=None):
        self.name = name
        self.description = description
        self.created_at = created_at


class CategoriesQuery(QueryTemplate[CategoriesQueryFilter, CategoriesQueryOrder]):
    pass


class CategoriesPaginatedQuery(PaginatedQueryTemplate[CategoriesQueryFilter, CategoriesQueryOrder]):
    pass