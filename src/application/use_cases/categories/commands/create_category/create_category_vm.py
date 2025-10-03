from typing import Optional
from domain.entities import Category
from application.commons.vms import BasicVm


class CreateCategoryVm(BasicVm):
    name: Optional[str] = None
    description: Optional[str] = None
    
    @classmethod
    def map_from_entities(cls, category:Category):
        return cls(
            id=category.id if isinstance(category.id, int) else str(category.id),
            name=category.name,
            description=category.description,
            created_at=category.created_at.strftime("%Y-%m-%d %H:%M:%S") if category.created_at else None
        )