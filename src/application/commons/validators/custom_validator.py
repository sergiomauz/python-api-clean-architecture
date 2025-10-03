from abc import ABC, abstractmethod


class CustomValidator(ABC):
    @abstractmethod
    def format_validation(self):
        pass
    

def validate_format_request_before(func):
    def wrapper(self, request: CustomValidator):
        if not isinstance(request, CustomValidator):
            raise TypeError("Input parameter must be a 'CustomValidator'")
        request.format_validation()
        
        return func(self, request)
    
    return wrapper    