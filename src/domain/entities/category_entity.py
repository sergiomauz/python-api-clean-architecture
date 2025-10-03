from dataclasses import dataclass
from typing import Optional, List, Any
from .bases import BaseWithIdEntity


@dataclass
class Category(BaseWithIdEntity):
    name: Optional[str] = None
    description: Optional[str] = None
    
    products: Optional[List[Any]] = None