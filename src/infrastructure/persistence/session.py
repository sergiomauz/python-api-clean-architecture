
from typing import Any
from contextlib import contextmanager, asynccontextmanager
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession


@contextmanager
def get_session_by_context(session_factory:sessionmaker) -> Session: # type: ignore
    session: Session = session_factory()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()    


@asynccontextmanager
async def get_async_session_by_context(session_factory:sessionmaker) -> AsyncSession:  # type: ignore
    session: AsyncSession = session_factory()
    try:
        yield session
        await session.commit()
    except:
        await session.rollback()
        raise
    finally:
        await session.close()        