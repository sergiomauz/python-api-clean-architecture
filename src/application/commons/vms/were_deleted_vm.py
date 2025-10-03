from pydantic import BaseModel


class WereDeletedVm(BaseModel):
    were_deleted: bool
    total_affected: int
