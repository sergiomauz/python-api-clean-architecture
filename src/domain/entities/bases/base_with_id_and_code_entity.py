
from dataclasses import dataclass
from typing import Optional
from .base_with_id_entity import BaseWithIdEntity


@dataclass
class BaseWithIdAndCodeEntity(BaseWithIdEntity):
    code: Optional[str] = None