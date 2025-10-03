
from typing import Optional
from commons.enums import OrderOperator
from domain.query_objects.utils import FilteringCriterion, QueryTemplate, PaginatedQueryTemplate


class PartnersQueryFilter:
    def __init__(self, 
                code:Optional[FilteringCriterion]=None, 
                name:Optional[FilteringCriterion]=None, 
                contact:Optional[FilteringCriterion]=None, 
                phone:Optional[FilteringCriterion]=None, 
                address:Optional[FilteringCriterion]=None, 
                email:Optional[FilteringCriterion]=None, 
                created_at:Optional[FilteringCriterion]=None):
        self.code = code
        self.name = name
        self.contact = contact
        self.phone = phone
        self.address = address
        self.email = email
        self.created_at = created_at
        

class PartnersQueryOrder:
    def __init__(self, 
                code:Optional[OrderOperator]=None,
                name:Optional[OrderOperator]=None,
                contact:Optional[OrderOperator]=None, 
                phone:Optional[OrderOperator]=None, 
                address:Optional[OrderOperator]=None, 
                email:Optional[OrderOperator]=None, 
                created_at:Optional[OrderOperator]=None):
        self.code = code
        self.name = name
        self.contact = contact
        self.phone = phone
        self.address = address
        self.email = email
        self.created_at = created_at


class PartnersQuery(QueryTemplate[PartnersQueryFilter, PartnersQueryOrder]):
    pass


class PartnersPaginatedQuery(PaginatedQueryTemplate[PartnersQueryFilter, PartnersQueryOrder]):
    pass