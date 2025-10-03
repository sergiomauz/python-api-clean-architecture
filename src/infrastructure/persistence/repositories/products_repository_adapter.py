from typing import List
from sqlalchemy import select, text, func, or_
from sqlalchemy.ext.asyncio import AsyncSession
from domain.entities import Product, Category
from domain.query_objects import ProductsQuery, ProductsPaginatedQuery
from infrastructure.persistence.models import ProductModel, CategoryModel
from infrastructure.persistence.repositories.bases import BaseWithIdAndCodeRepositoryAdapter
from application.abstractions.persistence import ProductsRepositoryPort


class ProductsRepositoryAdapter(ProductsRepositoryPort[Product, ProductModel],
                                BaseWithIdAndCodeRepositoryAdapter[Product, ProductModel]):

    def __init__(self, db_session:AsyncSession):
        super().__init__(Product, ProductModel, db_session)

    async def total_count_products_by_text_async(self, text_filter:str) -> int:
        counter = (
            select(func.count())
            .select_from(ProductModel)
            .where(
                or_(
                    ProductModel.name.ilike(f"%{text_filter}%"),
                    ProductModel.code.ilike(f"%{text_filter}%"),
                    ProductModel.description.ilike(f"%{text_filter}%")
                )            
            )
        )
        result = await self._session.execute(counter)
                
        return result.scalar_one()

    async def search_products_by_text_async(self, text_filter:str, current_page:int, page_size:int) -> List[Product]:
        offset_value = (current_page - 1) * page_size
        query = (
            select(ProductModel.id, ProductModel.code, 
                    ProductModel.name, ProductModel.description,
                    ProductModel.category_id, CategoryModel.name.label("category"),
                    ProductModel.created_at, ProductModel.modified_at)
            .outerjoin(CategoryModel, ProductModel.category_id == CategoryModel.id)
            .where(
                or_(
                    ProductModel.name.ilike(f"%{text_filter}%"),
                    ProductModel.code.ilike(f"%{text_filter}%"),
                    ProductModel.description.ilike(f"%{text_filter}%")
                )            
            )
            .order_by(ProductModel.created_at.asc())
            .offset(offset_value)
            .limit(page_size)
        )
        result = await self._session.execute(query)
        model_rows = result.all()        
        entity_rows = [
            Product(
                id=row.id,
                code=row.code,
                name=row.name,                
                description=row.description,
                category_id=row.category_id,
                category=Category(id=row.category_id, name=row.category),
                created_at=row.created_at,
                modified_at=row.modified_at,
            )
            for row in model_rows
        ]

        return entity_rows
    
    async def total_count_products_by_object_async(self, products_query:ProductsQuery) -> int:
        sql = "SELECT COUNT(*) FROM products pro "
        sql_filters = ""

        if products_query.filtering_criteria:
            if products_query.filtering_criteria.code:            
                code_operator = products_query.filtering_criteria.code.operator
                code_operand = products_query.filtering_criteria.code.operand
                sql_filters += f"pro.code {self.convert_operator_to_sql(code_operator)} {self.convert_operand_to_sql(code_operator, code_operand)} AND "

            if products_query.filtering_criteria.name:            
                name_operator = products_query.filtering_criteria.name.operator
                name_operand = products_query.filtering_criteria.name.operand
                sql_filters += f"pro.name {self.convert_operator_to_sql(name_operator)} {self.convert_operand_to_sql(name_operator, name_operand)} AND "
            
            if products_query.filtering_criteria.description:            
                description_operator = products_query.filtering_criteria.description.operator
                description_operand = products_query.filtering_criteria.description.operand
                sql_filters += f"pro.description {self.convert_operator_to_sql(description_operator)} {self.convert_operand_to_sql(description_operator, description_operand)} AND "

            if products_query.filtering_criteria.created_at:
                created_at_operator = products_query.filtering_criteria.created_at.operator
                created_at_operand = products_query.filtering_criteria.created_at.operand
                sql_filters += f"pro.created_at {self.convert_operator_to_sql(created_at_operator)} {self.convert_operand_to_sql(created_at_operator, created_at_operand)} AND "

            sql_filters = f"WHERE {sql_filters[:-5]} "
            sql += sql_filters
        try:
            result = await self._session.execute(text(sql))
            return result.scalar_one()
        except:
            await self._session.rollback()
            raise
        
    async def search_products_by_object_async(self, products_query:ProductsPaginatedQuery) -> List[Product]:
        offset_value = (products_query.current_page - 1) * products_query.page_size
        sql = """ 
            SELECT pro.id, pro.category_id, cat.name as category,
                    pro.code, pro.name, pro.description, 
                    pro.created_at, pro.modified_at
            FROM products pro 
                LEFT JOIN categories cat on pro.category_id = cat.id """
        sql_filters = ""
        sql_orders = ""
        sql_current_page = f"LIMIT {products_query.page_size} OFFSET {offset_value}"
        
        if products_query.filtering_criteria:
            if products_query.filtering_criteria.code:            
                code_operator = products_query.filtering_criteria.code.operator
                code_operand = products_query.filtering_criteria.code.operand
                sql_filters += f"pro.code {self.convert_operator_to_sql(code_operator)} {self.convert_operand_to_sql(code_operator, code_operand)} AND "
                            
            if products_query.filtering_criteria.name:            
                name_operator = products_query.filtering_criteria.name.operator
                name_operand = products_query.filtering_criteria.name.operand
                sql_filters += f"pro.name {self.convert_operator_to_sql(name_operator)} {self.convert_operand_to_sql(name_operator, name_operand)} AND "
            
            if products_query.filtering_criteria.category:            
                category_operator = products_query.filtering_criteria.category.operator
                category_operand = products_query.filtering_criteria.category.operand
                sql_filters += f"cat.name {self.convert_operator_to_sql(category_operator)} {self.convert_operand_to_sql(category_operator, category_operand)} AND "

            if products_query.filtering_criteria.description:            
                description_operator = products_query.filtering_criteria.description.operator
                description_operand = products_query.filtering_criteria.description.operand
                sql_filters += f"pro.description {self.convert_operator_to_sql(description_operator)} {self.convert_operand_to_sql(description_operator, description_operand)} AND "

            if products_query.filtering_criteria.created_at:
                created_at_operator = products_query.filtering_criteria.created_at.operator
                created_at_operand = products_query.filtering_criteria.created_at.operand
                sql_filters += f"pro.created_at {self.convert_operator_to_sql(created_at_operator)} {self.convert_operand_to_sql(created_at_operator, created_at_operand)} AND "
        
            sql_filters = f"WHERE {sql_filters[:-5]} "
            sql += sql_filters        
        
        if products_query.ordering_criteria:
            if products_query.ordering_criteria.code:
                sql_orders += f"pro.code {products_query.ordering_criteria.code.value}, "            
            if products_query.ordering_criteria.name:
                sql_orders += f"pro.name {products_query.ordering_criteria.name.value}, "
            if products_query.ordering_criteria.category:
                sql_orders += f"cat.name {products_query.ordering_criteria.category.value}, "                
            if products_query.ordering_criteria.description:
                sql_orders += f"pro.description {products_query.ordering_criteria.description.value}, "
            if products_query.ordering_criteria.created_at:
                sql_orders += f"pro.created_at {products_query.ordering_criteria.created_at.value}, "
            sql_orders = f"ORDER BY {sql_orders.rstrip(', ')} "    
        else:
            sql_orders = "ORDER BY pro.created_at "
        
        sql += sql_orders
        sql += sql_current_page        
        try:
            result = await self._session.execute(text(sql))
            rows = result.fetchall()
            return [
                Product(
                    id=row._mapping["id"], 
                    code=row._mapping["code"], 
                    name=row._mapping["name"], 
                    description=row._mapping["description"],
                    category_id=row._mapping["category_id"],
                    category=Category(id=row._mapping["category_id"], name=row._mapping["category"]),
                    created_at=row._mapping["created_at"],
                    modified_at=row._mapping["modified_at"]
                ) for row in rows
            ]
        except:
            await self._session.rollback()
            raise        
