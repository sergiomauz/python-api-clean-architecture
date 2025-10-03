
from datetime import datetime, timezone
from sqlalchemy import Column, String
from .base_with_id_model import BaseWithIdModel


class BaseWithIdAndCodeModel(BaseWithIdModel):
    __abstract__ = True

    code = Column(String(10), nullable=False, unique=True)