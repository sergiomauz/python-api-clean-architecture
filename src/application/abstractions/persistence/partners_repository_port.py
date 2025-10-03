from abc import abstractmethod
from typing import List
from domain.query_objects import PartnersQuery, PartnersPaginatedQuery
from application.abstractions.persistence.bases import (
    BaseWithIdAndCodeRepositoryPort, TEntity, TModel
)


class PartnersRepositoryPort(BaseWithIdAndCodeRepositoryPort[TEntity, TModel]):
    
    @abstractmethod
    async def total_count_partners_by_text_async(self, text_filter:str) -> int:
        pass
            
    @abstractmethod
    async def search_partners_by_text_async(self, text_filter:str, current_page:int, page_size:int) -> List[TEntity]:
        pass
    
    @abstractmethod
    async def total_count_partners_by_object_async(self, partners_query:PartnersQuery) -> int:
        pass
            
    @abstractmethod
    async def search_partners_by_object_async(self, partners_paginated_query:PartnersPaginatedQuery) -> List[TEntity]:
        pass
    