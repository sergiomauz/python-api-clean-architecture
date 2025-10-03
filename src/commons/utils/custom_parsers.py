import uuid
import numbers
from datetime import datetime
from typing import Any, Optional, List, Union


class CustomParsers:
    
    @staticmethod
    def to_datetime(value:str) -> Optional[datetime]:        
        valid_formats = [
            "%Y-%m-%d",
            "%Y-%m-%d %H:%M:%S",
            "%d/%m/%Y",
            "%d/%m/%Y %H:%M:%S",
            "%Y/%m/%d",
            "%Y/%m/%d %H:%M:%S",
            "%m-%d-%Y",
            "%m/%d/%Y",
        ]
        for valid_format in valid_formats:
            try:
                return datetime.strptime(value, valid_format)
            except ValueError:
                continue
        
        return None

    @staticmethod    
    def is_valid_datetime(value:str) -> bool:
        valid_formats = [
            "%Y-%m-%d",
            "%Y-%m-%d %H:%M:%S",
            "%d/%m/%Y",
            "%d/%m/%Y %H:%M:%S",
            "%Y/%m/%d",
            "%Y/%m/%d %H:%M:%S",
            "%m-%d-%Y",
            "%m/%d/%Y",
        ]        
        for fmt in valid_formats:
            try:
                datetime.strptime(value, fmt)
                return True
            except ValueError:
                continue
        
        return False        

    @staticmethod
    def are_valid_datetimes(value:Union[str,List[str]]) -> bool:
        if isinstance(value, str):
            return CustomParsers.is_valid_datetime(value)

        if isinstance(value, list) and all(isinstance(v, str) for v in value):
            return all(CustomParsers.is_valid_datetime(v) for v in value)

        return False

    @staticmethod
    def to_uuid(value:str) -> Optional[Any]:
        try:
            return uuid.UUID(value)
        except ValueError:
            return None

    @staticmethod
    def is_valid_uuid(value:str) -> bool:
        try:
            uuid.UUID(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def are_valid_uuids(value:Union[str,List[str]]) -> bool:
        if isinstance(value, str):
            return CustomParsers.is_valid_uuid(value)

        if isinstance(value, list) and all(isinstance(v, str) for v in value):
            return all(CustomParsers.is_valid_uuid(v) for v in value)

        return False
    
    @staticmethod
    def are_same_type(value: List[Any]) -> bool:
        if not value:
            return False

        first = value[0]
        if isinstance(first, numbers.Number):
            return all(isinstance(x, numbers.Number) for x in value)

        return all(isinstance(x, type(first)) for x in value)
