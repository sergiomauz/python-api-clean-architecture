from typing import Generic, TypeVar, Optional
from .paginated_request_params import PaginatedRequestParams


TFilter = TypeVar("TFilter")
TOrder = TypeVar("TOrder")

class ObjectRequestParams(PaginatedRequestParams, Generic[TFilter, TOrder]):
    filtering_criteria: Optional[TFilter] = None
    ordering_criteria: Optional[TOrder] = None
