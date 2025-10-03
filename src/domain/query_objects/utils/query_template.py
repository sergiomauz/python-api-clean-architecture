
from typing import Generic, TypeVar, Optional


TFilter = TypeVar("TFilter")
TOrder = TypeVar("TOrder")

class QueryTemplate(Generic[TFilter, TOrder]):
    def __init__(self, filtering_criteria:Optional[TFilter]=None, ordering_criteria:Optional[TOrder]=None):
        self.filtering_criteria = filtering_criteria
        self.ordering_criteria = ordering_criteria
