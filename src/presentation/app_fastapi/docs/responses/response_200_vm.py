from pydantic import BaseModel
from typing import Generic, TypeVar


T = TypeVar("T") 

class Response200Vm(BaseModel, Generic[T]):
    message: str
    data: T
