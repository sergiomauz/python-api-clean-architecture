
from typing import Protocol


class DbTransactionsManagerPort(Protocol):

    def commit(self) -> None:
        pass
    
    def rollback(self) -> None:
        pass    
    
    async def commit_async(self) -> None:
        pass
    
    async def rollback_async(self) -> None:
        pass    