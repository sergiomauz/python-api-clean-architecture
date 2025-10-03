from typing import Optional
from domain.entities import Partner
from application.commons.vms import BasicVm


class SearchPartnersByTextVm(BasicVm):
    name: Optional[str] = None
    contact: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    email: Optional[str] = None
    
    @classmethod
    def map_from_entities(cls, partner:Partner):
        return cls(
            id=partner.id if isinstance(partner.id, int) else str(partner.id),
            name=partner.name,
            contact=partner.contact,
            phone=partner.phone,
            address=partner.address,
            email=partner.email,
            created_at=partner.created_at.strftime("%Y-%m-%d %H:%M:%S") if partner.created_at else None,
            modified_at=partner.modified_at.strftime("%Y-%m-%d %H:%M:%S") if partner.modified_at else None
        )