from pydantic import BaseModel
from typing import Optional


class SearchCategoriesByObjectOrderingDto(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
