import logging
from http import HTTPStatus
from application.abstractions.persistence import ProductsRepositoryPort, CategoriesRepositoryPort
from application.commons.validators import validate_format_request_before
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .get_product_by_id_query import GetProductByIdQuery
from .get_product_by_id_vm import GetProductByIdVm


logger = logging.getLogger(__name__)

class GetProductByIdUseCase:

    def __init__(self, products_repository:ProductsRepositoryPort,
                 categories_repository:CategoriesRepositoryPort):
        self._products_repository = products_repository
        self._categories_repository = categories_repository

    @validate_format_request_before
    async def execute(self, query:GetProductByIdQuery):
        data = await self._products_repository.get_by_id_async(query.id)
        if not data:
            raise CustomValidationError(
                None,
                [CustomValidationErrorVm(
                    error_code=ErrorConstants.GET_PRODUCT_BY_ID_CONTENT00001.error_code,
                    property_name=ErrorConstants.GET_PRODUCT_BY_ID_CONTENT00001.property_name,                    
                    error_message=ErrorConstants.GET_PRODUCT_BY_ID_CONTENT00001.error_message
                )],
                HTTPStatus.NOT_FOUND.value
            )
        data.category = await self._categories_repository.get_by_id_async(data.category_id)
        vm = GetProductByIdVm.map_from_entities(data)

        return vm.model_dump()
