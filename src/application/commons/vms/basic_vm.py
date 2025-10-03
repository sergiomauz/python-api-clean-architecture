from pydantic import BaseModel
from typing import Optional, Any


class BasicVm(BaseModel):
    id: Optional[int|Any] = None
    created_at: Optional[str] = None
    modified_at: Optional[str] = None
