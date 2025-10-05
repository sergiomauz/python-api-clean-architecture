from sqlalchemy import Column, Integer, ForeignKey, String, Float, DateTime
from sqlalchemy.orm import relationship
from .bases import BaseWithUuidModel


class MovementModel(BaseWithUuidModel):
    __tablename__ = "movements"
    
    partner_id = Column(Integer, ForeignKey("partners.id", ondelete="SET NULL"), nullable=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="SET NULL"), nullable=True)
    
    movement_date = Column(DateTime, nullable=False)
    quantity = Column(Float, nullable=False)
    movement_type = Column(String(3), nullable=False)
    
    partner = relationship("PartnerModel", back_populates="movements")
    product = relationship("ProductModel", back_populates="movements")
