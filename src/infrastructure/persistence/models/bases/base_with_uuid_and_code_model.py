
from datetime import datetime, timezone
from sqlalchemy import Column, String
from .base_with_uuid_model import BaseWithUuidModel


class BaseWithUuidAndCodeModel(BaseWithUuidModel):
    __abstract__ = True

    code = Column(String(10), nullable=False, unique=True)