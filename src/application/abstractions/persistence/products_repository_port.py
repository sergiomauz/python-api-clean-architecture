from abc import abstractmethod
from typing import List
from domain.query_objects import ProductsQuery, ProductsPaginatedQuery
from application.abstractions.persistence.bases import (
    BaseWithIdAndCodeRepositoryPort, TEntity, TModel
)


class ProductsRepositoryPort(BaseWithIdAndCodeRepositoryPort[TEntity, TModel]):
    
    @abstractmethod
    async def total_count_products_by_text_async(self, text_filter:str) -> int:
        pass
            
    @abstractmethod
    async def search_products_by_text_async(self, text_filter:str, current_page:int, page_size:int) -> List[TEntity]:
        pass
    
    @abstractmethod
    async def total_count_products_by_object_async(self, products_query:ProductsQuery) -> int:
        pass
            
    @abstractmethod
    async def search_products_by_object_async(self, products_paginated_query:ProductsPaginatedQuery) -> List[TEntity]:
        pass
    