from pydantic import BaseModel
from typing import Optional


class SearchMovementsByObjectOrderingDto(BaseModel):
    partner: Optional[str] = None
    product: Optional[str] = None
    quantity: Optional[str] = None
    movement_type: Optional[str] = None
    movement_date: Optional[str] = None
    created_at: Optional[str] = None
