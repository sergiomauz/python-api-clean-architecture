from dataclasses import dataclass
from typing import Optional, List, Any
from .bases import BaseWithIdAndCodeEntity


@dataclass
class Product(BaseWithIdAndCodeEntity):
    category_id: Optional[int] = None    
    name: Optional[str] = None
    description: Optional[str] = None
        
    category: Optional[Any] = None
    movements: Optional[List[Any]] = None