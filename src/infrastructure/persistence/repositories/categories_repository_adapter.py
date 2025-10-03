from typing import List
from sqlalchemy import select, text, func, or_
from sqlalchemy.ext.asyncio import AsyncSession
from domain.entities import Category
from domain.query_objects import CategoriesQuery, CategoriesPaginatedQuery
from infrastructure.persistence.models import CategoryModel
from infrastructure.persistence.repositories.bases import BaseWithIdRepositoryAdapter
from application.abstractions.persistence import CategoriesRepositoryPort


class CategoriesRepositoryAdapter(CategoriesRepositoryPort[Category, CategoryModel],
                                  BaseWithIdRepositoryAdapter[Category, CategoryModel]):

    def __init__(self, db_session:AsyncSession):
        super().__init__(Category, CategoryModel, db_session)

    async def total_count_categories_by_text_async(self, text_filter:str) -> int:
        counter = (
            select(func.count())
            .select_from(CategoryModel)
            .where(
                or_(
                    CategoryModel.name.ilike(f"%{text_filter}%"),
                    CategoryModel.description.ilike(f"%{text_filter}%")
                )            
            )
        )
        result = await self._session.execute(counter)
                
        return result.scalar_one()

    async def search_categories_by_text_async(self, text_filter:str, current_page:int, page_size:int) -> List[Category]:
        offset_value = (current_page - 1) * page_size
        query = (
            select(CategoryModel.id, CategoryModel.name, CategoryModel.description, 
                   CategoryModel.created_at, CategoryModel.modified_at)
            .where(
                or_(
                    CategoryModel.name.ilike(f"%{text_filter}%"),
                    CategoryModel.description.ilike(f"%{text_filter}%")
                )            
            )
            .order_by(CategoryModel.created_at.asc())
            .offset(offset_value)
            .limit(page_size)
        )
        result = await self._session.execute(query)
        model_rows = result.all()        
        entity_rows = [
            Category(
                id=row.id,
                name=row.name,
                description=row.description,
                created_at=row.created_at,
                modified_at=row.modified_at,
            )
            for row in model_rows
        ]

        return entity_rows
    
    async def total_count_categories_by_object_async(self, categories_query:CategoriesQuery) -> int:
        sql = "SELECT COUNT(*) FROM categories ca "
        sql_filters = ""
                       
        if categories_query.filtering_criteria:
            if categories_query.filtering_criteria.name:            
                name_operator = categories_query.filtering_criteria.name.operator
                name_operand = categories_query.filtering_criteria.name.operand
                sql_filters += f"ca.name {self.convert_operator_to_sql(name_operator)} {self.convert_operand_to_sql(name_operator, name_operand)} AND "
            
            if categories_query.filtering_criteria.description:            
                description_operator = categories_query.filtering_criteria.description.operator
                description_operand = categories_query.filtering_criteria.description.operand
                sql_filters += f"ca.description {self.convert_operator_to_sql(description_operator)} {self.convert_operand_to_sql(description_operator, description_operand)} AND "

            if categories_query.filtering_criteria.created_at:
                created_at_operator = categories_query.filtering_criteria.created_at.operator
                created_at_operand = categories_query.filtering_criteria.created_at.operand
                sql_filters += f"(ca.created_at {self.convert_operator_to_sql(created_at_operator)} {self.convert_operand_to_sql(created_at_operator, created_at_operand)}) AND "

            sql_filters = f"WHERE {sql_filters[:-5]} "
            sql += sql_filters
        try:
            result = await self._session.execute(text(sql))
            return result.scalar_one()
        except:
            await self._session.rollback()
            raise

    async def search_categories_by_object_async(self, categories_query:CategoriesPaginatedQuery) -> List[Category]:
        offset_value = (categories_query.current_page - 1) * categories_query.page_size
        sql = "SELECT * FROM categories ca "
        sql_filters = ""
        sql_orders = ""
        sql_current_page = f"LIMIT {categories_query.page_size} OFFSET {offset_value}"
        
        if categories_query.filtering_criteria:
            if categories_query.filtering_criteria.name:            
                name_operator = categories_query.filtering_criteria.name.operator
                name_operand = categories_query.filtering_criteria.name.operand
                sql_filters += f"ca.name {self.convert_operator_to_sql(name_operator)} {self.convert_operand_to_sql(name_operator, name_operand)} AND "
            
            if categories_query.filtering_criteria.description:            
                description_operator = categories_query.filtering_criteria.description.operator
                description_operand = categories_query.filtering_criteria.description.operand
                sql_filters += f"ca.description {self.convert_operator_to_sql(description_operator)} {self.convert_operand_to_sql(description_operator, description_operand)} AND "

            if categories_query.filtering_criteria.created_at:
                created_at_operator = categories_query.filtering_criteria.created_at.operator
                created_at_operand = categories_query.filtering_criteria.created_at.operand
                sql_filters += f"(ca.created_at {self.convert_operator_to_sql(created_at_operator)} {self.convert_operand_to_sql(created_at_operator, created_at_operand)}) AND "
                
            sql_filters = f"WHERE {sql_filters[:-5]} "
            sql += sql_filters        
        
        if categories_query.ordering_criteria:
            if categories_query.ordering_criteria.name:
                sql_orders += f"ca.name {categories_query.ordering_criteria.name.value}, "
            if categories_query.ordering_criteria.description:
                sql_orders += f"ca.description {categories_query.ordering_criteria.description.value}, "
            if categories_query.ordering_criteria.created_at:
                sql_orders += f"ca.created_at {categories_query.ordering_criteria.created_at.value}, "                
        if len(sql_orders) > 0:
            sql_orders = f"ORDER BY {sql_orders.rstrip(', ')} "    
        else:
            sql_orders = "ORDER BY ca.created_at "
        
        sql += sql_orders
        sql += sql_current_page        
        try:
            result = await self._session.execute(text(sql))
            rows = result.fetchall()
            return [
                Category(
                    id=row._mapping["id"], 
                    name=row._mapping["name"], 
                    description=row._mapping["description"],
                    created_at=row._mapping["created_at"],
                    modified_at=row._mapping["modified_at"]
                ) for row in rows
            ]
        except:
            await self._session.rollback()
            raise        
