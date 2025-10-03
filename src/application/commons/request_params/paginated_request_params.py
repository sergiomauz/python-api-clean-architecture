from pydantic import BaseModel
from typing import Optional


class PaginatedRequestParams(BaseModel):
    current_page: Optional[int] = None
    page_size: Optional[int] = None
