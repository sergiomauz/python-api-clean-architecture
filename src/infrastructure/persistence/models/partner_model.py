
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .bases import BaseWithIdAndCodeModel


class PartnerModel(BaseWithIdAndCodeModel):
    __tablename__ = "partners"
    
    name = Column(String(350), nullable=False)
    contact = Column(String(200), nullable=False)
    phone = Column(String(15), nullable=False)
    address = Column(String(500), nullable=False)
    email = Column(String(100), nullable=False)
    
    movements = relationship("MovementModel", back_populates="partner")
