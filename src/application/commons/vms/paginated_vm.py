
from typing import Generic, TypeVar, List
from pydantic import BaseModel
import math


T = TypeVar("T")

class PaginatedVm(BaseModel, Generic[T]):
    items: List[T]
    total_items: int
    current_page: int
    page_size: int
    total_pages: int
    
    def __init__(self, items:List[T], total_items:int, current_page:int, page_size:int):
        if page_size > 0:
            total_pages = math.ceil(total_items / page_size)
            if total_pages == 0:
                total_pages = 1
        else:
            page_size = total_items
            total_pages = 1

        super().__init__(
            items=items,
            total_items=total_items,
            current_page=current_page,
            page_size=page_size,
            total_pages=total_pages,
        )