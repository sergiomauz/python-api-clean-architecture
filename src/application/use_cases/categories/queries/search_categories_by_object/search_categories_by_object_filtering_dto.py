from pydantic import BaseModel
from typing import Optional
from application.commons.request_params import FilteringCriterionRequestParams


class SearchCategoriesByObjectFilteringDto(BaseModel):
    name: Optional[FilteringCriterionRequestParams] = None
    description: Optional[FilteringCriterionRequestParams] = None
    created_at: Optional[FilteringCriterionRequestParams] = None
