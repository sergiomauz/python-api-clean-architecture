from pydantic import BaseModel
from typing import Optional


class CreateCategoryDto(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None