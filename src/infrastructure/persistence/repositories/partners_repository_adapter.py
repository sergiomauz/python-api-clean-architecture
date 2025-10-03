
from typing import List
from sqlalchemy import select, text, func, or_
from sqlalchemy.ext.asyncio import AsyncSession
from domain.entities import Partner
from domain.query_objects import PartnersQuery, PartnersPaginatedQuery
from infrastructure.persistence.models import PartnerModel
from infrastructure.persistence.repositories.bases import BaseWithIdAndCodeRepositoryAdapter
from application.abstractions.persistence import PartnersRepositoryPort


class PartnersRepositoryAdapter(PartnersRepositoryPort[Partner, PartnerModel],
                                BaseWithIdAndCodeRepositoryAdapter[Partner, PartnerModel]):

    def __init__(self, db_session:AsyncSession):
        super().__init__(Partner, PartnerModel, db_session)

    async def total_count_partners_by_text_async(self, text_filter:str) -> int:
        counter = (
            select(func.count())
            .select_from(PartnerModel)
            .where(
                or_(
                    PartnerModel.name.ilike(f"%{text_filter}%"),
                    PartnerModel.contact.ilike(f"%{text_filter}%"),
                    PartnerModel.phone.ilike(f"%{text_filter}%"),
                    PartnerModel.address.ilike(f"%{text_filter}%"),
                    PartnerModel.email.ilike(f"%{text_filter}%")
                )            
            )
        )
        result = await self._session.execute(counter)
                
        return result.scalar_one()

    async def search_partners_by_text_async(self, text_filter:str, current_page:int, page_size:int) -> List[Partner]:
        offset_value = (current_page - 1) * page_size
        query = (
            select(PartnerModel.id, PartnerModel.name, PartnerModel.contact, 
                    PartnerModel.phone, PartnerModel.address, PartnerModel.email, 
                    PartnerModel.created_at, PartnerModel.modified_at)
            .where(
                or_(
                    PartnerModel.name.ilike(f"%{text_filter}%"),
                    PartnerModel.contact.ilike(f"%{text_filter}%"),
                    PartnerModel.phone.ilike(f"%{text_filter}%"),
                    PartnerModel.address.ilike(f"%{text_filter}%"),
                    PartnerModel.email.ilike(f"%{text_filter}%")
                )
            )
            .order_by(PartnerModel.created_at.asc())
            .offset(offset_value)
            .limit(page_size)
        )
        result = await self._session.execute(query)
        model_rows = result.all()        
        entity_rows = [
            Partner(
                id=row.id,
                code=row.code,
                name=row.name,
                contact=row.contact,
                phone=row.phone,
                address=row.address,
                email=row.email,
                created_at=row.created_at,
                modified_at=row.modified_at
            )
            for row in model_rows
        ]

        return entity_rows
    
    async def total_count_partners_by_object_async(self, partners_query:PartnersQuery) -> int:
        sql = "SELECT COUNT(*) FROM partners pa "
        sql_filters = ""

        if partners_query.filtering_criteria:
            if partners_query.filtering_criteria.code:
                code_operator = partners_query.filtering_criteria.code.operator
                code_operand = partners_query.filtering_criteria.code.operand
                sql_filters += f"pa.code {self.convert_operator_to_sql(code_operator)} {self.convert_operand_to_sql(code_operator, code_operand)} AND "
            
            if partners_query.filtering_criteria.name:            
                name_operator = partners_query.filtering_criteria.name.operator
                name_operand = partners_query.filtering_criteria.name.operand
                sql_filters += f"pa.name {self.convert_operator_to_sql(name_operator)} {self.convert_operand_to_sql(name_operator, name_operand)} AND "
                            
            if partners_query.filtering_criteria.contact:            
                contact_operator = partners_query.filtering_criteria.contact.operator
                contact_operand = partners_query.filtering_criteria.contact.operand
                sql_filters += f"pa.contact {self.convert_operator_to_sql(contact_operator)} {self.convert_operand_to_sql(contact_operator, contact_operand)} AND "

            if partners_query.filtering_criteria.phone:
                phone_operator = partners_query.filtering_criteria.phone.operator
                phone_operand = partners_query.filtering_criteria.phone.operand
                sql_filters += f"pa.phone {self.convert_operator_to_sql(phone_operator)} {self.convert_operand_to_sql(phone_operator, phone_operand)} AND "

            if partners_query.filtering_criteria.address:
                address_operator = partners_query.filtering_criteria.address.operator
                address_operand = partners_query.filtering_criteria.address.operand
                sql_filters += f"pa.address {self.convert_operator_to_sql(address_operator)} {self.convert_operand_to_sql(address_operator, address_operand)} AND "

            if partners_query.filtering_criteria.email:
                email_operator = partners_query.filtering_criteria.email.operator
                email_operand = partners_query.filtering_criteria.email.operand
                sql_filters += f"pa.email {self.convert_operator_to_sql(email_operator)} {self.convert_operand_to_sql(email_operator, email_operand)} AND "
                
            if partners_query.filtering_criteria.created_at:
                created_at_operator = partners_query.filtering_criteria.created_at.operator
                created_at_operand = partners_query.filtering_criteria.created_at.operand
                sql_filters += f"pa.created_at {self.convert_operator_to_sql(created_at_operator)} {self.convert_operand_to_sql(created_at_operator, created_at_operand)} AND "

            sql_filters = f"WHERE {sql_filters[:-5]} "
            sql += sql_filters
        try:
            result = await self._session.execute(text(sql))
            return result.scalar_one()
        except:
            await self._session.rollback()
            raise
        
    async def search_partners_by_object_async(self, partners_query:PartnersPaginatedQuery) -> List[Partner]:
        offset_value = (partners_query.current_page - 1) * partners_query.page_size
        sql = "SELECT * FROM partners pa "
        sql_filters = ""
        sql_orders = ""
        sql_current_page = f"LIMIT {partners_query.page_size} OFFSET {offset_value}"
        
        if partners_query.filtering_criteria:
            if partners_query.filtering_criteria.code:
                code_operator = partners_query.filtering_criteria.code.operator
                code_operand = partners_query.filtering_criteria.code.operand
                sql_filters += f"pa.code {self.convert_operator_to_sql(code_operator)} {self.convert_operand_to_sql(code_operator, code_operand)} AND "

            if partners_query.filtering_criteria.name:            
                name_operator = partners_query.filtering_criteria.name.operator
                name_operand = partners_query.filtering_criteria.name.operand
                sql_filters += f"pa.name {self.convert_operator_to_sql(name_operator)} {self.convert_operand_to_sql(name_operator, name_operand)} AND "
                            
            if partners_query.filtering_criteria.contact:            
                contact_operator = partners_query.filtering_criteria.contact.operator
                contact_operand = partners_query.filtering_criteria.contact.operand
                sql_filters += f"pa.contact {self.convert_operator_to_sql(contact_operator)} {self.convert_operand_to_sql(contact_operator, contact_operand)} AND "

            if partners_query.filtering_criteria.phone:
                phone_operator = partners_query.filtering_criteria.phone.operator
                phone_operand = partners_query.filtering_criteria.phone.operand
                sql_filters += f"pa.phone {self.convert_operator_to_sql(phone_operator)} {self.convert_operand_to_sql(phone_operator, phone_operand)} AND "

            if partners_query.filtering_criteria.address:
                address_operator = partners_query.filtering_criteria.address.operator
                address_operand = partners_query.filtering_criteria.address.operand
                sql_filters += f"pa.address {self.convert_operator_to_sql(address_operator)} {self.convert_operand_to_sql(address_operator, address_operand)} AND "

            if partners_query.filtering_criteria.email:
                email_operator = partners_query.filtering_criteria.email.operator
                email_operand = partners_query.filtering_criteria.email.operand
                sql_filters += f"pa.email {self.convert_operator_to_sql(email_operator)} {self.convert_operand_to_sql(email_operator, email_operand)} AND "

            if partners_query.filtering_criteria.created_at:
                created_at_operator = partners_query.filtering_criteria.created_at.operator
                created_at_operand = partners_query.filtering_criteria.created_at.operand
                sql_filters += f"pa.created_at {self.convert_operator_to_sql(created_at_operator)} {self.convert_operand_to_sql(created_at_operator, created_at_operand)} AND "

            sql_filters = f"WHERE {sql_filters[:-5]} "
            sql += sql_filters        

        if partners_query.ordering_criteria:
            if partners_query.ordering_criteria.code:
                sql_orders += f"pa.code {partners_query.ordering_criteria.code.value}, "
            if partners_query.ordering_criteria.name:
                sql_orders += f"pa.name {partners_query.ordering_criteria.name.value}, "
            if partners_query.ordering_criteria.contact:
                sql_orders += f"pa.contact {partners_query.ordering_criteria.contact.value}, "
            if partners_query.ordering_criteria.phone:
                sql_orders += f"pa.phone {partners_query.ordering_criteria.phone.value}, "
            if partners_query.ordering_criteria.address:
                sql_orders += f"pa.address {partners_query.ordering_criteria.address.value}, "
            if partners_query.ordering_criteria.email:
                sql_orders += f"pa.email {partners_query.ordering_criteria.email.value}, "                                
            if partners_query.ordering_criteria.created_at:
                sql_orders += f"pa.created_at {partners_query.ordering_criteria.created_at.value}, "
            sql_orders = f"ORDER BY {sql_orders.rstrip(', ')} "    
        else:
            sql_orders = "ORDER BY pa.created_at "
        
        sql += sql_orders
        sql += sql_current_page        
        try:
            result = await self._session.execute(text(sql))
            rows = result.fetchall()
            return [
                Partner(
                    id=row._mapping["id"], 
                    code=row._mapping["code"], 
                    name=row._mapping["name"], 
                    contact=row._mapping["contact"],
                    phone=row._mapping["phone"],
                    address=row._mapping["address"],
                    email=row._mapping["email"],
                    created_at=row._mapping["created_at"],
                    modified_at=row._mapping["modified_at"]
                ) for row in rows
            ]
        except Exception as e:
            await self._session.rollback()
            raise e