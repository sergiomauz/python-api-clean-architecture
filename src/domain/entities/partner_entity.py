from dataclasses import dataclass
from typing import Optional, List, Any
from .bases import BaseWithIdAndCodeEntity


@dataclass
class Partner(BaseWithIdAndCodeEntity):
    name: Optional[str] = None
    contact: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    email: Optional[str] = None

    movements: Optional[List[Any]] = None