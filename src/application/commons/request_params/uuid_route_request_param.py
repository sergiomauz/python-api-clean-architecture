from pydantic import BaseModel
from typing import Optional


class UuidRouteRequestParam(BaseModel):
    id: Optional[str] = None
