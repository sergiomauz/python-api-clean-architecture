
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, DateTime
from infrastructure.persistence import Base


class BaseWithIdModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    modified_at = Column(DateTime, default=None, onupdate=datetime.now(timezone.utc), nullable=True)
