
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional


TEntity = TypeVar("TEntity")
TModel = TypeVar("TModel") 

class BaseWithIdRepositoryPort(ABC, Generic[TEntity, TModel]):
        
    @abstractmethod
    async def create_async(self, entity_object:TEntity) -> TEntity:
        pass
    
    @abstractmethod
    async def create_and_commit_async(self, entity_object:TEntity) -> TEntity:
        pass    
                
    @abstractmethod
    async def delete_async(self, ids: List[int]) -> int:
        pass
    
    @abstractmethod
    async def delete_and_commit_async(self, ids:List[int]) -> int:
        pass

    @abstractmethod
    async def update_async(self, entity_object:TEntity) -> int:
        pass
    
    @abstractmethod
    async def update_and_commit_async(self, entity_object:TEntity) -> int:
        pass
        
    @abstractmethod
    async def get_by_id_async(self, id:int) -> Optional[TEntity]:
        pass
