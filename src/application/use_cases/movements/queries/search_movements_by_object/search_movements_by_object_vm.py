from typing import Optional
from domain.entities import Movement
from application.commons.vms import BasicVm


class SearchMovementsByObjectVm(BasicVm):
    partner_id: Optional[int] = None
    partner: Optional[str] = None
    product_id: Optional[int] = None
    product: Optional[str] = None
    quantity: Optional[float] = None
    movement_type: Optional[str] = None
    movement_date: Optional[str] = None
            
    @classmethod
    def map_from_entities(cls, movement:Movement):
        return cls(
            id=movement.id if isinstance(movement.id, int) else str(movement.id),
            partner_id=movement.partner_id,
            partner=movement.partner.name if movement.partner is not None else None,
            product_id=movement.product_id,
            product=movement.product.name if movement.product is not None else None,
            quantity=movement.quantity,
            movement_type=movement.movement_type,
            movement_date=movement.movement_date.strftime("%Y-%m-%d %H:%M:%S") if movement.movement_date else None,
            created_at=movement.created_at.strftime("%Y-%m-%d %H:%M:%S") if movement.created_at else None,
            modified_at=movement.modified_at.strftime("%Y-%m-%d %H:%M:%S") if movement.modified_at else None
        )