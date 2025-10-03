
import os
import asyncio
from logger_config import setup_async_logger
from di_container_beta import DiContainerBeta
from infrastructure.persistence import check_db_connection_async, get_async_session_by_context
from presentation.app_flask.exceptions_handler import exceptions_handler
from presentation.app_flask.extended_flask import ExtendedFlask
from presentation.app_flask.routes import routes


PORT = 8000 if not os.environ.get("API_PORT") else int(os.environ.get("API_PORT"))
DEBUG = True if os.environ.get("DEBUG") == "1" else False

# Initialize dependencies injectors from container
container = DiContainerBeta()
container.config.from_yaml("config.yml")
container.wire(packages=["presentation.app_flask.routes"])

#
app = ExtendedFlask(__name__)
app.register_error_handler(Exception, exceptions_handler)
app.include_blueprints(routes)


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
                app.run(debug=True, host="0.0.0.0", port=PORT)
            else:
                app.run(host="0.0.0.0", port=PORT)
        finally:
            listener.stop()


if __name__ == "__main__":
    asyncio.run(main())
