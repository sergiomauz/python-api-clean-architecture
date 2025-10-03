from pydantic import BaseModel
from typing import List, Optional


class UuidsBodyRequestParam(BaseModel):
    ids: Optional[List[str]] = None
