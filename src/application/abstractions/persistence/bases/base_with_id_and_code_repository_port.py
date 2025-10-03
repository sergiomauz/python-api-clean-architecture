from abc import abstractmethod
from typing import Optional
from application.abstractions.persistence.bases import BaseWithIdRepositoryPort, TEntity, TModel


class BaseWithIdAndCodeRepositoryPort(BaseWithIdRepositoryPort[TEntity, TModel]):
        
    @abstractmethod
    async def get_by_code_async(self, code:str) -> Optional[TEntity]:
        pass    