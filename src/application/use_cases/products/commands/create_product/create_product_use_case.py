import logging
from http import HTTPStatus
from domain.entities import Product
from application.abstractions.persistence import ProductsRepositoryPort, CategoriesRepositoryPort
from application.commons.validators import validate_format_request_before
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .create_product_command import CreateProductCommand
from .create_product_vm import CreateProductVm


logger = logging.getLogger(__name__)

class CreateProductUseCase:

    def __init__(self, products_repository:ProductsRepositoryPort, categories_repository:CategoriesRepositoryPort):
        self._products_repository = products_repository
        self._categories_repository = categories_repository

    @validate_format_request_before
    async def execute(self, command:CreateProductCommand):
        existing_category = await self._categories_repository.get_by_id_async(command.category_id)
        if not existing_category:
            raise CustomValidationError(
                None,
                [CustomValidationErrorVm(
                    error_code=ErrorConstants.CREATE_PRODUCT_CONTENT00001.error_code,
                    property_name=ErrorConstants.CREATE_PRODUCT_CONTENT00001.property_name,                    
                    error_message=ErrorConstants.CREATE_PRODUCT_CONTENT00001.error_message
                )],
                HTTPStatus.CONFLICT.value)            

        existing_product_by_code = await self._products_repository.get_by_code_async(command.code)
        if existing_product_by_code:
            raise CustomValidationError(
                None,
                [CustomValidationErrorVm(
                    error_code=ErrorConstants.CREATE_PRODUCT_CONTENT00002.error_code,
                    property_name=ErrorConstants.CREATE_PRODUCT_CONTENT00002.property_name,                    
                    error_message=ErrorConstants.CREATE_PRODUCT_CONTENT00002.error_message
                )],
                HTTPStatus.CONFLICT.value)

        created_product = await self._products_repository.create_and_commit_async(
            Product(
                category_id=command.category_id,
                code=command.code,
                name=command.name,
                description=command.description
            )
        )
        vm = CreateProductVm.map_from_entities(created_product)

        return vm.model_dump()
