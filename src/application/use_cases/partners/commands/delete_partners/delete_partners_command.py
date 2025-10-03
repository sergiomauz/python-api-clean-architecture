from http import HTTPStatus
from application.commons.queries import IdsQuery
from application.exceptions.errors import CustomValidationError
from .delete_partner_route import DeletePartnerRoute
from .delete_partners_dto import DeletePartnersDto


class DeletePartnersCommand(IdsQuery):

    def __init__(self, route:DeletePartnerRoute, dto:DeletePartnersDto):
        if route and route.id:
            super().__init__(ids=[route.id])
        elif dto and dto.ids and len(dto.ids) > 0:
            super().__init__(ids=dto.ids)

    def format_validation(self):
        errors = super().format_validation()
        if errors:
            raise CustomValidationError(
                None,
                errors, 
                HTTPStatus.UNPROCESSABLE_ENTITY.value)   

        return errors