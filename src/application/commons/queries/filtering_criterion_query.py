from commons.enums import FilterOperator
from commons.utils import CustomParsers
from application.commons.request_params import FilteringCriterionRequestParams


class FilteringCriterionQuery:
    
    def __init__(self, dto:FilteringCriterionRequestParams):
        self.operator = dto.operator
        self.operand = dto.operand

    def is_valid_filtering_operation(self) -> bool:
        filter_operator = FilterOperator.from_value(self.operator)
        
        if not filter_operator:
            return False
        
        if self.operand is None:
            return filter_operator in {
                FilterOperator.EQUALS, FilterOperator.NOT_EQUALS
            }
        
        # Is boolean?
        if isinstance(self.operand, bool):
            return filter_operator in {
                FilterOperator.EQUALS, FilterOperator.NOT_EQUALS
            }
        
        # Is number?
        if isinstance(self.operand, (int, float)):
            return filter_operator in {
                FilterOperator.EQUALS, FilterOperator.NOT_EQUALS,
                FilterOperator.GREATER_THAN, FilterOperator.LESS_THAN,
                FilterOperator.GREATER_THAN_OR_EQUAL, FilterOperator.LESS_THAN_OR_EQUAL                
            } or (len(filter_operator) == 2 and filter_operator == FilterOperator.BETWEEN)
        
        # Is string?
        if isinstance(self.operand, str):
            if CustomParsers.are_valid_datetimes(self.operand):
                return filter_operator in {
                    FilterOperator.EQUALS, FilterOperator.NOT_EQUALS,
                    FilterOperator.GREATER_THAN, FilterOperator.LESS_THAN,
                    FilterOperator.GREATER_THAN_OR_EQUAL, FilterOperator.LESS_THAN_OR_EQUAL
                }         
            else:
                return filter_operator in {
                    FilterOperator.EQUALS, FilterOperator.NOT_EQUALS,
                    FilterOperator.CONTAINS, FilterOperator.STARTS_WITH,
                    FilterOperator.ENDS_WITH                    
                }
        
        # Is an array?
        if isinstance(self.operand, list) and len(self.operand) > 0:
            if isinstance(self.operand[0], str):
                are_valid_datetimes = CustomParsers.are_valid_datetimes(self.operand)
                if are_valid_datetimes:
                    return filter_operator == FilterOperator.IN or (len(self.operand) == 2 and FilterOperator.BETWEEN)
                else:
                    return filter_operator == FilterOperator.IN    
            else:
                return filter_operator == FilterOperator.IN
                
        return False
