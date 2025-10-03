
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class BaseWithIdEntity:
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None
