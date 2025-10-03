from pydantic import BaseModel
from typing import Optional
from application.commons.request_params import FilteringCriterionRequestParams


class SearchProductsByObjectFilteringDto(BaseModel):
    code: Optional[FilteringCriterionRequestParams] = None
    name: Optional[FilteringCriterionRequestParams] = None
    category: Optional[FilteringCriterionRequestParams] = None
    description: Optional[FilteringCriterionRequestParams] = None
    created_at: Optional[FilteringCriterionRequestParams] = None
