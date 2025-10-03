from pydantic import BaseModel
from typing import Optional
from application.commons.request_params import FilteringCriterionRequestParams


class SearchPartnersByObjectFilteringDto(BaseModel):
    code: Optional[FilteringCriterionRequestParams] = None
    name: Optional[FilteringCriterionRequestParams] = None
    contact: Optional[FilteringCriterionRequestParams] = None
    phone: Optional[FilteringCriterionRequestParams] = None
    address: Optional[FilteringCriterionRequestParams] = None
    email: Optional[FilteringCriterionRequestParams] = None
    created_at: Optional[FilteringCriterionRequestParams] = None