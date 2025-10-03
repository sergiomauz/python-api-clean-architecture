
from typing import Generic, TypeVar, Optional


TFilter = TypeVar("TFilter")
TOrder = TypeVar("TOrder")

class PaginatedQueryTemplate(Generic[TFilter, TOrder]):
    def __init__(self, 
                 filtering_criteria:Optional[TFilter]=None, 
                 ordering_criteria:Optional[TOrder]=None, 
                 current_page: Optional[int]=None,
                 page_size:Optional[int]=None):
        self.filtering_criteria = filtering_criteria
        self.ordering_criteria = ordering_criteria
        self.current_page = current_page if current_page else 1
        self.page_size = page_size if page_size else 20
