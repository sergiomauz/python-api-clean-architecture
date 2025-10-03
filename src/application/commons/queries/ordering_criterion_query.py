from commons.enums import OrderOperator


class OrderingCriterionQuery:
    
    def __init__(self, operator:str):
        self.operator = operator

    def is_valid_ordering_operation(self) -> bool:
        if OrderOperator.from_value(self.operator):
            return True
        return False