import logging
from http import HTTPStatus
from domain.entities import Product
from application.abstractions.persistence import ProductsRepositoryPort, CategoriesRepositoryPort
from application.commons.validators import validate_format_request_before
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .update_product_command import UpdateProductCommand
from .update_product_vm import UpdateProductVm


logger = logging.getLogger(__name__)

class UpdateProductUseCase:

    def __init__(self, products_repository:ProductsRepositoryPort, categories_repository:CategoriesRepositoryPort):
        self._products_repository = products_repository
        self._categories_repository = categories_repository
    
    @validate_format_request_before
    async def execute(self, command:UpdateProductCommand):
        existing_product = await self._products_repository.get_by_id_async(command.id)
        if not existing_product:
            raise CustomValidationError(
                None,
                [CustomValidationErrorVm(
                    error_code=ErrorConstants.UPDATE_PRODUCT_CONTENT00001.error_code,
                    property_name=ErrorConstants.UPDATE_PRODUCT_CONTENT00001.property_name,                    
                    error_message=ErrorConstants.UPDATE_PRODUCT_CONTENT00001.error_message
                )],
                HTTPStatus.NOT_FOUND.value)
        
        if command.category_id:
            existing_category = await self._categories_repository.get_by_id_async(command.category_id)
            if not existing_category:
                raise CustomValidationError(
                    None,
                    [CustomValidationErrorVm(
                        error_code=ErrorConstants.UPDATE_PRODUCT_CONTENT00002.error_code,
                        property_name=ErrorConstants.UPDATE_PRODUCT_CONTENT00002.property_name,                    
                        error_message=ErrorConstants.UPDATE_PRODUCT_CONTENT00002.error_message
                    )],
                    HTTPStatus.CONFLICT.value)
            existing_product.category_id = command.category_id
        
        if command.code:
            existing_product_by_code = await self._products_repository.get_by_code_async(command.code)
            if existing_product_by_code and command.id != existing_product_by_code.id:
                raise CustomValidationError(
                    None,
                    [CustomValidationErrorVm(
                        error_code=ErrorConstants.UPDATE_PRODUCT_CONTENT00003.error_code,
                        property_name=ErrorConstants.UPDATE_PRODUCT_CONTENT00003.property_name,                    
                        error_message=ErrorConstants.UPDATE_PRODUCT_CONTENT00003.error_message
                    )],
                    HTTPStatus.CONFLICT.value)
            existing_product.code = command.code
        
        if command.name: 
            existing_product.name = command.name
        
        if command.description:
            existing_product.description = command.description

        await self._products_repository.update_and_commit_async(            
            Product(
                id=existing_product.id,
                category_id=existing_product.category_id,
                code=existing_product.code,
                name=existing_product.name,
                description=existing_product.description                
            )
        )
        vm = UpdateProductVm.map_from_entities(existing_product)

        return vm.model_dump()
