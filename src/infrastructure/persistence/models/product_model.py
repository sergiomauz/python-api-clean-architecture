from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from .bases import BaseWithIdAndCodeModel


class ProductModel(BaseWithIdAndCodeModel):
    __tablename__ = "products"
    
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    name = Column(String(75), nullable=False)
    description = Column(String(150), nullable=True)
    
    movements = relationship("MovementModel", back_populates="product")
    category = relationship("CategoryModel", back_populates="products")
