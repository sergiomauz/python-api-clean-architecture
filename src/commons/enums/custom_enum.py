from enum import Enum


class CustomEnum(Enum):

    @classmethod
    def selection(cls):
        return [(e.value, e.name.capitalize()) for e in cls]
    
    @classmethod
    def from_value(cls, value:str):
        try:
            return cls(value.lower())
        except ValueError:
            return None