
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.engine import Engine


def create_sqlalchemy_engine(connection_string:str) -> Engine:
    return create_engine(
        connection_string,
        pool_size=10,
        max_overflow=0,
        pool_timeout=30,
        pool_recycle=1800
    )


def create_sqlalchemy_engine_async(connection_string:str) -> AsyncEngine:
    return create_async_engine(
        connection_string,
        pool_size=10,
        max_overflow=0,
        pool_timeout=30,
        pool_recycle=1800
    )
