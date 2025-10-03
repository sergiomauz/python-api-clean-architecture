import logging
from application.abstractions.persistence import ProductsRepositoryPort
from application.commons.validators import validate_format_request_before
from .delete_products_command import DeleteProductsCommand
from .delete_products_vm import DeleteProductsVm


logger = logging.getLogger(__name__)

class DeleteProductsUseCase:

    def __init__(self, products_repository:ProductsRepositoryPort):
        self._products_repository = products_repository

    @validate_format_request_before
    async def execute(self, command:DeleteProductsCommand):
        affected_rows = await self._products_repository.delete_and_commit_async(command.ids)
        vm = DeleteProductsVm(
            were_deleted=(affected_rows > 0),
            total_affected=affected_rows
        )

        return vm.model_dump()