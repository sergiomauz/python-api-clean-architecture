
from functools import wraps
from flask import request, jsonify


def basic_authentication(func):
    """
        ToDo: DocString
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        
        if not auth_header or not auth_header.startswith("Basic "):
            return jsonify({"error": "Token inválido"}), 401
        
        # Get credentials
        encoded_credentials = auth_header.split(" ")[1]
        
        # Continue with endpoint
        return func(*args, **kwargs)
    
    return wrapper


async def basic_authentication_async(func):
    """
        ToDo: DocString
    """    
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        
        if not auth_header or not auth_header.startswith("Basic "):
            return jsonify({"error": "Token inválido"}), 401
        
        # Get credentials
        encoded_credentials = auth_header.split(" ")[1]
        
        # Continue with endpoint
        return func(*args, **kwargs)
    
    return wrapper