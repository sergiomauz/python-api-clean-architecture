from pydantic import BaseModel
from typing import Optional, Any


class FilteringCriterionRequestParams(BaseModel):
    operator: Any
    operand: Optional[Any] = None