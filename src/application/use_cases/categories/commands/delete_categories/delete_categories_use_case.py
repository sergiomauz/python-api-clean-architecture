import logging
from application.abstractions.persistence import CategoriesRepositoryPort
from application.commons.validators import validate_format_request_before
from .delete_categories_command import DeleteCategoriesCommand
from .delete_categories_vm import DeleteCategoriesVm


logger = logging.getLogger(__name__)

class DeleteCategoriesUseCase:
    
    def __init__(self, categories_repository:CategoriesRepositoryPort):
        self._categories_repository = categories_repository

    @validate_format_request_before
    async def execute(self, command:DeleteCategoriesCommand):
        affected_rows = await self._categories_repository.delete_and_commit_async(command.ids)
        vm = DeleteCategoriesVm(
            were_deleted=(affected_rows > 0),
            total_affected=affected_rows
        )
        
        return vm.model_dump()