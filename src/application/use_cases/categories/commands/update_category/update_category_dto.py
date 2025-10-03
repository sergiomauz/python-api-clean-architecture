from pydantic import BaseModel
from typing import Optional


class UpdateCategoryDto(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None