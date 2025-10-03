
import logging
from werkzeug.exceptions import HTTPException
from application.exceptions.errors import CustomValidationError
from presentation.app_flask.responses import ResponseValidationError


logger = logging.getLogger(__name__)

def exceptions_handler(exception:Exception):
    """ ToDo: DocString """    
    if isinstance(exception, CustomValidationError):
        return ResponseValidationError(exception)

    if isinstance(exception, HTTPException):
        return {
            "message": str(exception)
        }, exception.code

    logger.error(f"Unhandled exception: {str(exception)}")
    return {
        "message": "Server error, try again later.",
    }, 500
