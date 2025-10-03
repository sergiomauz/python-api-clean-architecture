
import os
import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from di_container_beta import DiContainerBeta
from logger_config import setup_async_logger
from infrastructure.persistence import check_db_connection_async, get_async_session_by_context
from presentation.app_fastapi.exceptions_handler import exceptions_handler, default_validation_exception_handler
from presentation.app_fastapi.routes import router as routes


PORT = 8000 if not os.environ.get("API_PORT") else int(os.environ.get("API_PORT"))
DEBUG = True if os.environ.get("DEBUG") == "1" else False

# Intialize dependencies injectors from container
container = DiContainerBeta()
container.config.from_yaml("config.yml")
container.wire(packages=["presentation.app_fastapi.routes"])

#
app = FastAPI(
    title="Hello FastAPI",
    description="Hello FastAPI",
    version="1.0"
)
app.add_exception_handler(Exception, exceptions_handler)
app.add_exception_handler(RequestValidationError, default_validation_exception_handler)
app.include_router(routes)


async def main():
    # Check db connection
    async with get_async_session_by_context(container.session_factory_async()) as session:
        start_app = await check_db_connection_async(session)

    # If all requirements were accomplished
    if start_app:
        # Start logging and run app
        listener = setup_async_logger()
        try:
            if DEBUG:
                uvicorn.run("main_fastapi:app", host="0.0.0.0", reload=True, port=PORT)
            else:
                uvicorn.run("main_fastapi:app", host="0.0.0.0", port=PORT)
        finally:
            listener.stop()


if __name__ == "__main__":
    asyncio.run(main())
