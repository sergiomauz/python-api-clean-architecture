
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from application.abstractions.persistence import DbTransactionsManagerPort


class DbTransactionsManagerAdapter(DbTransactionsManagerPort):
    
    def __init__(self, db_session):
        if not isinstance(db_session, (Session, AsyncSession)):
            raise TypeError(
                f"db_session must be an instance of Session or AsyncSession, got {type(db_session)}"
            )
        self._session = db_session
        self._is_async = isinstance(db_session, AsyncSession)


    def commit(self):
        if self._is_async:
            raise RuntimeError("commit() is not available for AsyncSession. Use commit_async().")
        
        return self._session.commit()


    def rollback(self):
        if self._is_async:
            raise RuntimeError("rollback() is not available for AsyncSession. Use rollback_async().")
        
        return self._session.rollback()


    async def commit_async(self):
        if not self._is_async:
            raise RuntimeError("commit_async() is only available for AsyncSession.")
        
        return await self._session.commit()


    async def rollback_async(self):
        if not self._is_async:
            raise RuntimeError("rollback_async() is only available for AsyncSession.")
        
        return await self._session.rollback()
