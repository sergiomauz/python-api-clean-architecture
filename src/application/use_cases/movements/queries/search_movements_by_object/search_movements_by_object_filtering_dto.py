from pydantic import BaseModel
from typing import Optional
from application.commons.request_params import FilteringCriterionRequestParams


class SearchMovementsByObjectFilteringDto(BaseModel):
    partner: Optional[FilteringCriterionRequestParams] = None
    product: Optional[FilteringCriterionRequestParams] = None
    quantity: Optional[FilteringCriterionRequestParams] = None
    movement_type: Optional[FilteringCriterionRequestParams] = None
    movement_date: Optional[FilteringCriterionRequestParams] = None
    created_at: Optional[FilteringCriterionRequestParams] = None