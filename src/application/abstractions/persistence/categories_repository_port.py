from abc import abstractmethod
from typing import List
from domain.query_objects import CategoriesQuery, CategoriesPaginatedQuery
from application.abstractions.persistence.bases import (
    BaseWithIdRepositoryPort, TEntity, TModel
)


class CategoriesRepositoryPort(BaseWithIdRepositoryPort[TEntity, TModel]):
        
    @abstractmethod
    async def total_count_categories_by_text_async(self, text_filter:str) -> int:
        pass
            
    @abstractmethod
    async def search_categories_by_text_async(self, text_filter:str, current_page:int, page_size:int) -> List[TEntity]:
        pass
    
    @abstractmethod
    async def total_count_categories_by_object_async(self, categories_query:CategoriesQuery) -> int:
        pass
            
    @abstractmethod
    async def search_categories_by_object_async(self, categories_paginated_query:CategoriesPaginatedQuery) -> List[TEntity]:
        pass
    