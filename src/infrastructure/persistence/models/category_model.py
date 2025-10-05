from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .bases import BaseWithIdModel


class CategoryModel(BaseWithIdModel):
    __tablename__ = "categories"
    
    name = Column(String(75), nullable=False)    
    description = Column(String(150), nullable=True)
    
    products = relationship("ProductModel", back_populates="category", cascade="all, delete")
