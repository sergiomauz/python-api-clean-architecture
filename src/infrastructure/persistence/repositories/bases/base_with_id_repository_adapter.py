from dataclasses import asdict
from typing import Type, List, Optional, Any
from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.inspection import inspect
from commons.enums import FilterOperator
from commons.utils import CustomParsers
from application.abstractions.persistence.bases import BaseWithIdRepositoryPort, TEntity, TModel


class BaseWithIdRepositoryAdapter(BaseWithIdRepositoryPort[TEntity, TModel]):
        
    def __init__(self, t_entity:Type[TEntity], t_model:Type[TModel], db_session:AsyncSession):
        self._t_entity = t_entity
        self._t_model = t_model
        self._session = db_session        

    def drop_nones(self, dict_object):
        if isinstance(dict_object, dict):
            cleaned = {}
            for k, v in dict_object.items():
                v_clean = self.drop_nones(v)
                if v_clean is not None:
                    cleaned[k] = v_clean
            return cleaned

        elif isinstance(dict_object, list):
            cleaned_list = []
            for item in dict_object:
                item_clean = self.drop_nones(item)
                if item_clean is not None:
                    cleaned_list.append(item_clean)
            return cleaned_list
        else:
            return dict_object

    def orm_to_dict(self, entity_model):
        return {c.key: getattr(entity_model, c.key) for c in inspect(entity_model).mapper.column_attrs}

    def convert_operator_to_sql(self, operator:FilterOperator):
        if operator in [FilterOperator.CONTAINS, FilterOperator.STARTS_WITH, FilterOperator.ENDS_WITH]:
            return "ILIKE"
        return operator.value

    def convert_operand_to_sql(self, operator:FilterOperator, operand:Optional[Any]):
        if operand is None:
            return "NULL"

        if isinstance(operand, (int, float, bool)):
            return operand
                
        if isinstance(operand, str):
            value_to_datetime = CustomParsers.to_datetime(operand)
            if value_to_datetime:
                return f"'%{operand}%'"
            else:
                if operator == FilterOperator.CONTAINS:
                    return f"'%{operand.replace("'", "''")}%'" if operand is not None else None
                elif operator == FilterOperator.STARTS_WITH:
                    return f"'{operand.replace("'", "''")}%'" if operand is not None else None
                elif operator == FilterOperator.ENDS_WITH:
                    return f"'%{operand.replace("'", "''")}'" if operand is not None else None
                else:
                    return f"'{operand.replace("'", "''")}'" if operand is not None else None
        
        if isinstance(operand, list):
            if len(operand) == 2 and operator == FilterOperator.BETWEEN:
                return f"{self.convert_operand_to_sql(FilterOperator.EQUALS, operand[0])} AND {self.convert_operand_to_sql(FilterOperator.EQUALS, operand[1])}"
            else:
                items = [self.convert_operand_to_sql(FilterOperator.EQUALS, element) for element in operand]
                return f"({', '.join(map(str, items))})"
                
        return None
    
    async def create_async(self, entity_object:TEntity) -> TEntity:
        new_object_model = self._t_model(**self.drop_nones(asdict(entity_object)))
        
        self._session.add(new_object_model)
        await self._session.flush()
        await self._session.refresh(new_object_model)
        
        return self._t_entity(**self.orm_to_dict(new_object_model)) 

    async def create_and_commit_async(self, entity_object:TEntity) -> TEntity:
        new_object_model = self._t_model(**self.drop_nones(asdict(entity_object)))
        
        try:            
            self._session.add(new_object_model)
            await self._session.commit()

            return self._t_entity(**self.orm_to_dict(new_object_model)) 
        except Exception as e:
            await self._session.rollback()
            raise e            
    
    async def delete_async(self, ids:List[int]) -> int:
        if not ids:
            return 0
        
        statement = delete(self._t_model).where(self._t_model.id.in_(ids))
        result = await self._session.execute(statement)
        
        return result.rowcount or 0
        
    async def delete_and_commit_async(self, ids:List[int]) -> int:
        if not ids:
            return 0
        
        try:            
            statement = delete(self._t_model).where(self._t_model.id.in_(ids))
            result = await self._session.execute(statement)
            await self._session.commit()
            
            return result.rowcount or 0
        except Exception as e:
            await self._session.rollback()
            raise e
                
    async def update_async(self, entity_object:TEntity) -> int:
        excluded_fields = {"id", "created_at", "modified_at"}
        model_columns = {c.name for c in self._t_model.__table__.columns}        
        values_to_update = {
            k: v 
            for k, v in asdict(entity_object).items() 
            if k in model_columns and k not in excluded_fields
        }
        
        statement = (
            update(self._t_model)
            .where(self._t_model.id == entity_object.id)
            .values(**values_to_update)
            .execution_options(synchronize_session=False)
        )
        affected = await self._session.execute(statement)
        
        return affected.rowcount or 0
   
    async def update_and_commit_async(self, entity_object:TEntity) -> int:
        excluded_fields = {"id", "created_at", "modified_at"}
        model_columns = {c.name for c in self._t_model.__table__.columns}        
        values_to_update = {
            k: v 
            for k, v in asdict(entity_object).items() 
            if k in model_columns and k not in excluded_fields
        }
        
        try:
            statement = (
                update(self._t_model)
                .where(self._t_model.id == entity_object.id)
                .values(**values_to_update)
                .execution_options(synchronize_session=False)
            )
            affected = await self._session.execute(statement)
            await self._session.commit()
            
            return affected.rowcount or 0
        except Exception as e:
            await self._session.rollback()
            raise e            
        
    async def get_by_id_async(self, id:int) -> Optional[TEntity]:
        existing_object_model = await self._session.get(self._t_model, id)
        if not existing_object_model:
            return None    
                
        return self._t_entity(**self.orm_to_dict(existing_object_model))
