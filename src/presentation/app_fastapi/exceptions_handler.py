
import logging
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException 
from application.exceptions.errors import CustomValidationError
from presentation.app_fastapi.responses import ResponseValidationError


logger = logging.getLogger(__name__)

async def exceptions_handler(request:Request, exception:Exception):
    """ ToDo: DocString """    
    if isinstance(exception, CustomValidationError):
        return ResponseValidationError(exception)

    if isinstance(exception, HTTPException):
        return JSONResponse(
            status_code=exception.status_code,
            content={
                "message": str(exception)
            })

    if isinstance(exception, AttributeError):
        if exception.obj is None:
            return JSONResponse(
                status_code=400,
                content={
                    "message": "Body can not be an empty object."
                })

    logger.error(f"Unhandled exception: {str(exception)}")
    return JSONResponse(
        status_code=500,
        content={
            "message": "Server error, try again later."
        })


async def default_validation_exception_handler(request:Request, exception:RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={
            "message": "Unable to parse request params. Recheck body, query strings and routes and try again."
        })