from typing import Optional
from commons.enums import OrderOperator
from domain.query_objects.utils import FilteringCriterion, QueryTemplate, PaginatedQueryTemplate


class MovementsQueryFilter:
    def __init__(self, 
                 partner:Optional[FilteringCriterion]=None, 
                 product:Optional[FilteringCriterion]=None, 
                 quantity:Optional[FilteringCriterion]=None, 
                 movement_type:Optional[FilteringCriterion]=None, 
                 movement_date:Optional[FilteringCriterion]=None, 
                 created_at:Optional[FilteringCriterion]=None):
        self.partner = partner
        self.product = product
        self.quantity = quantity
        self.movement_type = movement_type
        self.movement_date = movement_date
        self.created_at = created_at
        

class MovementsQueryOrder:
    def __init__(self, 
                 partner:Optional[OrderOperator]=None, 
                 product:Optional[OrderOperator]=None, 
                 quantity:Optional[OrderOperator]=None, 
                 movement_type:Optional[OrderOperator]=None, 
                 movement_date:Optional[OrderOperator]=None, 
                 created_at:Optional[OrderOperator]=None):
        self.partner = partner
        self.product = product
        self.quantity = quantity
        self.movement_type = movement_type
        self.movement_date = movement_date
        self.created_at = created_at


class MovementsQuery(QueryTemplate[MovementsQueryFilter, MovementsQueryOrder]):
    pass


class MovementsPaginatedQuery(PaginatedQueryTemplate[MovementsQueryFilter, MovementsQueryOrder]):
    pass