from typing import Optional
from .paginated_request_params import PaginatedRequestParams


class BasicSearchRequestParams(PaginatedRequestParams):
    text_filter: Optional[str] = None
    