from typing import Optional
from domain.entities import Movement, Product, Partner
from application.commons.vms import BasicVm


class CreateMovementVm(BasicVm):
    partner: Optional[str] = None
    product: Optional[str] = None
    movement_date: Optional[str] = None
    quantity: Optional[float] = None
    movement_type: Optional[str] = None

    @classmethod
    def map_from_entities(cls, movement:Movement, product:Product, partner:Partner):
        return cls(
            id=str(movement.id),
            partner=partner.name,
            product=product.name,
            movement_date=movement.movement_date.strftime("%Y-%m-%d %H:%M:%S"),
            quantity=movement.quantity,
            movement_type=movement.movement_type,
            created_at=movement.created_at.strftime("%Y-%m-%d %H:%M:%S") if movement.created_at else None
        )
