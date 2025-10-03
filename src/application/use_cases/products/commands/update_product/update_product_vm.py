from typing import Optional
from domain.entities import Product
from application.commons.vms import BasicVm


class UpdateProductVm(BasicVm):
    category_id: Optional[int] = None
    code: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    
    @classmethod
    def map_from_entities(cls, product:Product):
        return cls(
            id=product.id,
            category_id=product.category_id,
            code=product.code,
            name=product.name,
            description=product.description,            
            created_at=product.created_at.strftime("%Y-%m-%d %H:%M:%S") if product.created_at else None,
            modified_at=product.modified_at.strftime("%Y-%m-%d %H:%M:%S") if product.modified_at else None
        )
