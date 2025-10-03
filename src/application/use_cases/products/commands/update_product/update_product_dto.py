from pydantic import BaseModel
from typing import Optional


class UpdateProductDto(BaseModel):
    id: Optional[int] = None
    category_id: Optional[int] = None
    code: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None