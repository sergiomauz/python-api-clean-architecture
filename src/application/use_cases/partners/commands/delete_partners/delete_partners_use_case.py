import logging
from application.abstractions.persistence import PartnersRepositoryPort
from application.commons.validators import validate_format_request_before
from .delete_partners_command import DeletePartnersCommand
from .delete_partners_vm import DeletePartnersVm


logger = logging.getLogger(__name__)

class DeletePartnersUseCase:

    def __init__(self, partners_repository:PartnersRepositoryPort):
        self._partners_repository = partners_repository

    @validate_format_request_before
    async def execute(self, command:DeletePartnersCommand):
        affected_rows = await self._partners_repository.delete_and_commit_async(command.ids)
        vm = DeletePartnersVm(
            were_deleted=(affected_rows > 0),
            total_affected=affected_rows
        )

        return vm.model_dump()
