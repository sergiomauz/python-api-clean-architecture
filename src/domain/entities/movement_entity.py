from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any
from .bases import BaseWithIdEntity


@dataclass
class Movement(BaseWithIdEntity):
    partner_id: Optional[int] = None
    product_id: Optional[int] = None

    movement_date: Optional[datetime] = None
    quantity: Optional[float] = None
    movement_type: Optional[str] = None
    
    partner: Optional[Any] = None
    product: Optional[Any] = None