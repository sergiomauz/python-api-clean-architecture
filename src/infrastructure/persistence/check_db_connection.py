
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession


def check_db_connection(session:Session):
    """ ToDo: DocString """
    try:
        session.execute(text("SELECT 1"))
        return True
    except Exception as e:
        return False
    
async def check_db_connection_async(session:AsyncSession):
    """ ToDo: DocString """
    try:
        await session.execute(text("SELECT 1"))
        return True
    except Exception as e:
        return False    