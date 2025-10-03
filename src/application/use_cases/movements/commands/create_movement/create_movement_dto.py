from pydantic import BaseModel
from typing import Optional


class CreateMovementDto(BaseModel):
    partner_id: Optional[int] = None
    product_id: Optional[int] = None
    movement_date: Optional[str] = None
    quantity: Optional[float] = None
    movement_type: Optional[str] = None