from pydantic import BaseModel
from typing import Optional


class SearchProductsByObjectOrderingDto(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
