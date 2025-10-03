from typing import List
from sqlalchemy import select, text, cast, func, or_, String
from sqlalchemy.ext.asyncio import AsyncSession
from domain.entities import Movement, Product, Partner
from domain.query_objects import MovementsQuery, MovementsPaginatedQuery
from infrastructure.persistence.models import MovementModel, ProductModel, PartnerModel
from infrastructure.persistence.repositories.bases import BaseWithIdRepositoryAdapter
from application.abstractions.persistence import MovementsRepositoryPort


class MovementsRepositoryAdapter(MovementsRepositoryPort[Movement, MovementModel],
                                BaseWithIdRepositoryAdapter[Movement, MovementModel]):

    def __init__(self, db_session:AsyncSession):
        super().__init__(Movement, MovementModel, db_session)
    
    async def total_count_movements_by_text_async(self, text_filter:str) -> int:
        counter = (
            select(func.count())
            .select_from(MovementModel)            
            .outerjoin(ProductModel, MovementModel.product_id == ProductModel.id)
            .outerjoin(PartnerModel, MovementModel.partner_id == PartnerModel.id)
            .where(
                or_(
                    ProductModel.name.ilike(f"%{text_filter}%"),
                    PartnerModel.name.ilike(f"%{text_filter}%"),                    
                    cast(MovementModel.quantity, String).like(f"%{text_filter}%"),
                    func.to_char(MovementModel.movement_date, "YYYY-MM-DD").like(f"%{text_filter}%")
                )       
            )
        )
        result = await self._session.execute(counter)
                
        return result.scalar_one()

    async def search_movements_by_text_async(self, text_filter:str, current_page:int, page_size:int) -> List[Movement]:
        offset_value = (current_page - 1) * page_size
        query = (
            select(MovementModel.id, MovementModel.partner_id, MovementModel.product_id,
                   MovementModel.movement_date, MovementModel.movement_type, MovementModel.quantity,
                   ProductModel.name.label("product"), PartnerModel.name.label("partner"),
                   MovementModel.created_at, MovementModel.modified_at)
            .outerjoin(ProductModel, MovementModel.product_id == ProductModel.id)
            .outerjoin(PartnerModel, MovementModel.partner_id == PartnerModel.id)
            .where(
                or_(
                    ProductModel.name.ilike(f"%{text_filter}%"),
                    PartnerModel.name.ilike(f"%{text_filter}%"),                    
                    cast(MovementModel.quantity, String).like(f"%{text_filter}%"),
                    func.to_char(MovementModel.movement_date, "YYYY-MM-DD").like(f"%{text_filter}%")
                )
            )
            .order_by(MovementModel.created_at.asc())
            .offset(offset_value)
            .limit(page_size)
        )
        result = await self._session.execute(query)
        model_rows = result.all()        
        entity_rows = [
            Movement(
                id=row.id,
                partner_id=row.partner_id,
                partner=Partner(id=row.partner_id, name=row.partner),
                product_id=row.product_id,
                product=Product(id=row.product_id, name=row.product),
                movement_date=row.movement_date,
                quantity=row.quantity,
                movement_type=row.movement_type,                
                created_at=row.created_at,
                modified_at=row.modified_at,
            )
            for row in model_rows
        ]

        return entity_rows
    
    async def total_count_movements_by_object_async(self, movements_query:MovementsQuery) -> int:
        sql = """SELECT COUNT(*)
                FROM movements mo 
                    LEFT JOIN partners par ON mo.partner_id = par.id 
                    LEFT JOIN products pro ON mo.product_id = pro.id """
        sql_filters = ""

        if movements_query.filtering_criteria:
            if movements_query.filtering_criteria.partner:            
                partner_operator = movements_query.filtering_criteria.partner.operator
                partner_operand = movements_query.filtering_criteria.partner.operand
                sql_filters += f"par.name {self.convert_operator_to_sql(partner_operator)} {self.convert_operand_to_sql(partner_operator, partner_operand)} AND "
            
            if movements_query.filtering_criteria.product:            
                product_operator = movements_query.filtering_criteria.product.operator
                product_operand = movements_query.filtering_criteria.product.operand
                sql_filters += f"pro.name {self.convert_operator_to_sql(product_operator)} {self.convert_operand_to_sql(product_operator, product_operand)} AND "

            if movements_query.filtering_criteria.quantity:
                quantity_operator = movements_query.filtering_criteria.quantity.operator
                quantity_operand = movements_query.filtering_criteria.quantity.operand
                sql_filters += f"mo.quantity {self.convert_operator_to_sql(quantity_operator)} {self.convert_operand_to_sql(quantity_operator, quantity_operand)} AND "
                
            if movements_query.filtering_criteria.movement_type:
                movement_type_operator = movements_query.filtering_criteria.movement_type.operator
                movement_type_operand = movements_query.filtering_criteria.movement_type.operand
                sql_filters += f"mo.movement_type {self.convert_operator_to_sql(movement_type_operator)} {self.convert_operand_to_sql(movement_type_operator, movement_type_operand)} AND "                

            if movements_query.filtering_criteria.movement_date:
                movement_date_operator = movements_query.filtering_criteria.movement_date.operator
                movement_date_operand = movements_query.filtering_criteria.movement_date.operand
                sql_filters += f"mo.movement_date {self.convert_operator_to_sql(movement_date_operator)} {self.convert_operand_to_sql(movement_date_operator, movement_date_operand)} AND "

            if movements_query.filtering_criteria.created_at:
                created_at_operator = movements_query.filtering_criteria.created_at.operator
                created_at_operand = movements_query.filtering_criteria.created_at.operand
                sql_filters += f"mo.created_at {self.convert_operator_to_sql(created_at_operator)} {self.convert_operand_to_sql(created_at_operator, created_at_operand)} AND "

            sql_filters = f"WHERE {sql_filters[:-5]} "
            sql += sql_filters
        try:
            result = await self._session.execute(text(sql))
            return result.scalar_one()
        except:
            await self._session.rollback()
            raise
        
    async def search_movements_by_object_async(self, movements_query:MovementsPaginatedQuery) -> List[Movement]:
        offset_value = (movements_query.current_page - 1) * movements_query.page_size
        sql = """SELECT mo.id, mo.partner_id, par.name as partner,
                    mo.product_id, pro.name as product,
                    mo.movement_date, mo.quantity, mo.movement_type,
                    mo.created_at, mo.modified_at
                FROM movements mo 
                    LEFT JOIN partners par ON mo.partner_id = par.id 
                    LEFT JOIN products pro ON mo.product_id = pro.id """
        sql_filters = ""
        sql_orders = ""
        sql_current_page = f"LIMIT {movements_query.page_size} OFFSET {offset_value}"
        
        if movements_query.filtering_criteria:
            if movements_query.filtering_criteria.partner:            
                partner_operator = movements_query.filtering_criteria.partner.operator
                partner_operand = movements_query.filtering_criteria.partner.operand
                sql_filters += f"par.name {self.convert_operator_to_sql(partner_operator)} {self.convert_operand_to_sql(partner_operator, partner_operand)} AND "
            
            if movements_query.filtering_criteria.product:            
                product_operator = movements_query.filtering_criteria.product.operator
                product_operand = movements_query.filtering_criteria.product.operand
                sql_filters += f"pro.name {self.convert_operator_to_sql(product_operator)} {self.convert_operand_to_sql(product_operator, product_operand)} AND "

            if movements_query.filtering_criteria.quantity:
                quantity_operator = movements_query.filtering_criteria.quantity.operator
                quantity_operand = movements_query.filtering_criteria.quantity.operand
                sql_filters += f"mo.quantity {self.convert_operator_to_sql(quantity_operator)} {self.convert_operand_to_sql(quantity_operator, quantity_operand)} AND "
                
            if movements_query.filtering_criteria.movement_type:
                movement_type_operator = movements_query.filtering_criteria.movement_type.operator
                movement_type_operand = movements_query.filtering_criteria.movement_type.operand
                sql_filters += f"mo.movement_type {self.convert_operator_to_sql(movement_type_operator)} {self.convert_operand_to_sql(movement_type_operator, movement_type_operand)} AND "                

            if movements_query.filtering_criteria.movement_date:
                movement_date_operator = movements_query.filtering_criteria.movement_date.operator
                movement_date_operand = movements_query.filtering_criteria.movement_date.operand
                sql_filters += f"mo.movement_date {self.convert_operator_to_sql(movement_date_operator)} {self.convert_operand_to_sql(movement_date_operator, movement_date_operand)} AND "

            if movements_query.filtering_criteria.created_at:
                created_at_operator = movements_query.filtering_criteria.created_at.operator
                created_at_operand = movements_query.filtering_criteria.created_at.operand
                sql_filters += f"mo.created_at {self.convert_operator_to_sql(created_at_operator)} {self.convert_operand_to_sql(created_at_operator, created_at_operand)} AND "

            sql_filters = f"WHERE {sql_filters[:-5]} "
            sql += sql_filters        
        
        if movements_query.ordering_criteria:
            if movements_query.ordering_criteria.partner:
                sql_orders += f"par.name {movements_query.ordering_criteria.partner.value}, "
            if movements_query.ordering_criteria.product:
                sql_orders += f"pro.name {movements_query.ordering_criteria.product.value}, "
            if movements_query.ordering_criteria.quantity:
                sql_orders += f"mo.quantity {movements_query.ordering_criteria.quantity.value}, "                
            if movements_query.ordering_criteria.movement_type:
                sql_orders += f"mo.movement_type {movements_query.ordering_criteria.movement_type.value}, "
            if movements_query.ordering_criteria.movement_date:
                sql_orders += f"mo.movement_date {movements_query.ordering_criteria.movement_date.value}, "                
            if movements_query.ordering_criteria.created_at:
                sql_orders += f"mo.created_at {movements_query.ordering_criteria.created_at.value}, "
            sql_orders = f"ORDER BY {sql_orders.rstrip(', ')} "
        else:
            sql_orders = "ORDER BY mo.movement_date "
        
        sql += sql_orders
        sql += sql_current_page        
        try:
            result = await self._session.execute(text(sql))
            rows = result.fetchall()
            return [
                Movement(
                    id=row._mapping["id"],
                    partner_id=row._mapping["partner_id"],
                    partner=Partner(id=row._mapping["partner_id"], name=row._mapping["partner"]),
                    product_id=row._mapping["product_id"],
                    product=Product(id=row._mapping["product_id"], name=row._mapping["product"]),
                    movement_date=row._mapping["movement_date"],
                    quantity=row._mapping["quantity"],
                    movement_type=row._mapping["movement_type"],
                    created_at=row._mapping["created_at"],
                    modified_at=row._mapping["modified_at"]
                ) for row in rows
            ]
        except:
            await self._session.rollback()
            raise        
