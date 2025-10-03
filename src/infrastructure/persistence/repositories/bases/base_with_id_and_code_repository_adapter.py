from typing import Type, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from application.abstractions.persistence.bases import BaseWithIdAndCodeRepositoryPort, TEntity, TModel
from .base_with_id_repository_adapter import BaseWithIdRepositoryAdapter


class BaseWithIdAndCodeRepositoryAdapter(BaseWithIdAndCodeRepositoryPort[TEntity, TModel],
                                        BaseWithIdRepositoryAdapter[TEntity, TModel]):
        
    def __init__(self, t_entity:Type[TEntity], t_model:Type[TModel], db_session:AsyncSession):
        self._t_entity = t_entity
        self._t_model = t_model
        self._session = db_session
        
    async def get_by_code_async(self, code:str) -> Optional[TEntity]:
        try:
            statement = select(self._t_model).where(self._t_model.code == code)
            result = await self._session.execute(statement)        
            existing_object_model = result.scalars().first()
            if not existing_object_model:
                return None
                    
            return self._t_entity(**self.orm_to_dict(existing_object_model))
        except Exception as e:
            await self._session.rollback()
            raise e            