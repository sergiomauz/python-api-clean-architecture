from typing import Optional
from commons.enums import OrderOperator, FilterOperator
from domain.query_objects.utils import FilteringCriterion
from application.commons.queries import FilteringCriterionQuery, OrderingCriterionQuery


class QueryBuilder:
    
    @classmethod
    def filtering_builder(cls, field:Optional[FilteringCriterionQuery]=None) -> FilteringCriterion|None:
        return FilteringCriterion(
            operator=FilterOperator.from_value(field.operator),
            operand=field.operand
        ) if field is not None else None
        
    @classmethod
    def ordering_builder(cls, field:Optional[OrderingCriterionQuery]=None) -> OrderOperator|None:
        return OrderOperator.from_value(
            field.operator
        ) if field is not None else None