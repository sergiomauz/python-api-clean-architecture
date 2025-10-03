
from abc import abstractmethod
from typing import List
from domain.query_objects import MovementsQuery, MovementsPaginatedQuery
from application.abstractions.persistence.bases import BaseWithIdRepositoryPort, TEntity, TModel


class MovementsRepositoryPort(BaseWithIdRepositoryPort[TEntity, TModel]):
    
    @abstractmethod
    async def total_count_movements_by_text_async(self, text_filter:str) -> int:
        pass
            
    @abstractmethod
    async def search_movements_by_text_async(self, text_filter:str, current_page:int, page_size:int) -> List[TEntity]:
        pass
    
    @abstractmethod
    async def total_count_movements_by_object_async(self, movements_query:MovementsQuery) -> int:
        pass
            
    @abstractmethod
    async def search_movements_by_object_async(self, movements_paginated_query:MovementsPaginatedQuery) -> List[TEntity]:
        pass
    