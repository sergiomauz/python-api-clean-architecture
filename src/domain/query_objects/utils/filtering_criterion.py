from typing import Optional, Any
from commons.enums import FilterOperator


class FilteringCriterion:
    
    def __init__(self, operator:FilterOperator, operand:Optional[Any]=None):
        self.operator = operator
        self.operand = operand  
