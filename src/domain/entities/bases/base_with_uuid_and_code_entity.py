
from dataclasses import dataclass
from typing import Optional
from .base_with_uuid_entity import BaseWithUuidEntity


@dataclass
class BaseWithUuidAndCodeEntity(BaseWithUuidEntity):
    code: Optional[str] = None