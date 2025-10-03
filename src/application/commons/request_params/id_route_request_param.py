from pydantic import BaseModel
from typing import Optional


class IdRouteRequestParam(BaseModel):
    id: Optional[int] = None
