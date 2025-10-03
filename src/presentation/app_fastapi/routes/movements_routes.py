from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from di_container_beta import DiContainerBeta
from application.commons.vms import PaginatedVm
from application.use_cases.movements.commands.create_movement import (
    CreateMovementDto, CreateMovementCommand, CreateMovementUseCase, CreateMovementVm
)
from application.use_cases.movements.commands.delete_movements import (
    DeleteMovementRoute, DeleteMovementsDto, DeleteMovementsCommand, DeleteMovementsUseCase, DeleteMovementsVm
)
from application.use_cases.movements.queries.get_movement_by_id import (
    GetMovementByIdRoute, GetMovementByIdQuery, GetMovementByIdUseCase, GetMovementByIdVm
)
from application.use_cases.movements.queries.search_movements_by_text import (
    SearchMovementsByTextRequestParams, SearchMovementsByTextQuery, SearchMovementsByTextUseCase, SearchMovementsByTextVm
)
from application.use_cases.movements.queries.search_movements_by_object import (
    SearchMovementsByObjectDto, SearchMovementsByObjectQuery, SearchMovementsByObjectUseCase, SearchMovementsByObjectVm
)
from presentation.app_fastapi.responses import ResponseOk
from presentation.app_fastapi.docs.responses import Response200Vm, Response422Vm, Response409Vm


router = APIRouter(
    prefix="",
    tags=["Movements"]
)

@router.post("/movements", response_model=Response200Vm[CreateMovementVm], responses={422:{"model":Response422Vm}, 409:{"model":Response409Vm}})
@inject
async def create_movement(
    dto: CreateMovementDto=None,
    use_case: CreateMovementUseCase=Depends(Provide[DiContainerBeta.create_movement_use_case])
):
    """ ToDo: DocString """
    command = CreateMovementCommand(dto)
    vm = await use_case.execute(command)        
    return ResponseOk("'create_movement', from extended FastAPI!", vm)

@router.get("/movements", response_model=Response200Vm[PaginatedVm[SearchMovementsByTextVm]], responses={422:{"model":Response422Vm}})
@inject
async def search_movements_by_text(
    request_params: SearchMovementsByTextRequestParams=Depends(),
    use_case: SearchMovementsByTextUseCase=Depends(Provide[DiContainerBeta.search_movements_by_text_use_case])
):
    """ ToDo: DocString """
    query = SearchMovementsByTextQuery(request_params)
    vm = await use_case.execute(query)
    return ResponseOk("'search_movements_by_text', from extended FastAPI!", vm)

@router.delete("/movements/{id}", response_model=Response200Vm[DeleteMovementsVm], responses={422:{"model":Response422Vm}})
@inject
async def delete_movement(
    id: str,
    use_case: DeleteMovementsUseCase=Depends(Provide[DiContainerBeta.delete_movements_use_case])
):
    """ ToDo: DocString """
    route = DeleteMovementRoute(id=id)
    command = DeleteMovementsCommand(route, None)
    vm = await use_case.execute(command)
    return ResponseOk("'delete_movements', from extended FastAPI!", vm)

@router.get("/movements/{id}", response_model=Response200Vm[GetMovementByIdVm], responses={422:{"model":Response422Vm}})
@inject
async def get_movement_by_id(
    id: str,
    use_case: GetMovementByIdUseCase=Depends(Provide[DiContainerBeta.get_movement_by_id_use_case])
):
    """ ToDo: DocString """
    route = GetMovementByIdRoute(id=id)
    query = GetMovementByIdQuery(route)
    vm = await use_case.execute(query)
    return ResponseOk("'get_movement_by_id', from extended FastAPI!", vm)

@router.post("/movements/delete", response_model=Response200Vm[DeleteMovementsVm], responses={422:{"model":Response422Vm}})
@inject
async def delete_movements(
    dto: DeleteMovementsDto=None,
    use_case: DeleteMovementsUseCase=Depends(Provide[DiContainerBeta.delete_movements_use_case])
):
    """ ToDo: DocString """
    command = DeleteMovementsCommand(None, dto)
    vm = await use_case.execute(command)        
    return ResponseOk("'delete_movements', from extended FastAPI!", vm)

@router.post("/movements/search", response_model=Response200Vm[PaginatedVm[SearchMovementsByObjectVm]], responses={422:{"model":Response422Vm}})
@inject
async def search_movements_by_object(
    dto: SearchMovementsByObjectDto=None,
    use_case: SearchMovementsByObjectUseCase=Depends(Provide[DiContainerBeta.search_movements_by_object])
):
    """ ToDo: DocString """    
    query = SearchMovementsByObjectQuery(dto)
    vm = await use_case.execute(query)
    return ResponseOk("'search_movements_by_object', from extended FastAPI!", vm)



