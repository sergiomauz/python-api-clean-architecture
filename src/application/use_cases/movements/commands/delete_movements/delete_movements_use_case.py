import logging
from application.abstractions.persistence import MovementsRepositoryPort
from application.commons.validators import validate_format_request_before
from .delete_movements_command import DeleteMovementsCommand
from .delete_movements_vm import DeleteMovementsVm


logger = logging.getLogger(__name__)

class DeleteMovementsUseCase:

    def __init__(self, movements_repository:MovementsRepositoryPort):
        self._movements_repository = movements_repository

    @validate_format_request_before
    async def execute(self, command:DeleteMovementsCommand):
        affected_rows = await self._movements_repository.delete_and_commit_async(command.ids)
        vm = DeleteMovementsVm(
            were_deleted=(affected_rows > 0),
            total_affected=affected_rows
        )

        return vm.model_dump()
