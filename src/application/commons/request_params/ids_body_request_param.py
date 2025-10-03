from pydantic import BaseModel
from typing import List, Optional


class IdsBodyRequestParam(BaseModel):
    ids: Optional[List[int]] = None
