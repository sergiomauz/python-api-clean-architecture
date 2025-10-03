from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from di_container_beta import DiContainerBeta
from application.commons.vms import PaginatedVm
from application.use_cases.partners.commands.create_partner import (
    CreatePartnerDto, CreatePartnerCommand, CreatePartnerUseCase, CreatePartnerVm
)
from application.use_cases.partners.commands.delete_partners import (
    DeletePartnerRoute, DeletePartnersDto, DeletePartnersCommand, DeletePartnersUseCase, DeletePartnersVm
)
from application.use_cases.partners.commands.update_partner import (
    UpdatePartnerRoute,  UpdatePartnerDto, UpdatePartnerCommand, UpdatePartnerUseCase, UpdatePartnerVm
)
from application.use_cases.partners.queries.get_partner_by_id import (
    GetPartnerByIdRoute, GetPartnerByIdQuery, GetPartnerByIdUseCase, GetPartnerByIdVm
)
from application.use_cases.partners.queries.search_partners_by_text import (
    SearchPartnersByTextRequestParams, SearchPartnersByTextQuery, SearchPartnersByTextUseCase, SearchPartnersByTextVm
)
from application.use_cases.partners.queries.search_partners_by_object import (
    SearchPartnersByObjectDto, SearchPartnersByObjectQuery, SearchPartnersByObjectUseCase, SearchPartnersByObjectVm
)
from presentation.app_fastapi.responses import ResponseOk
from presentation.app_fastapi.docs.responses import Response200Vm, Response422Vm, Response409Vm


router = APIRouter(
    prefix="",
    tags=["Partners"]
)

@router.post("/partners", response_model=Response200Vm[CreatePartnerVm], responses={422:{"model":Response422Vm}, 409:{"model":Response409Vm}})
@inject
async def create_partner(
    dto: CreatePartnerDto=None,
    use_case: CreatePartnerUseCase=Depends(Provide[DiContainerBeta.create_partner_use_case])
):
    """ ToDo: DocString """
    command = CreatePartnerCommand(dto)
    vm = await use_case.execute(command)        
    return ResponseOk("'create_partner', from extended FastAPI!", vm)

@router.get("/partners", response_model=Response200Vm[PaginatedVm[SearchPartnersByTextVm]], responses={422:{"model":Response422Vm}})
@inject
async def search_partners_by_text(
    request_params: SearchPartnersByTextRequestParams=Depends(),
    use_case: SearchPartnersByTextUseCase=Depends(Provide[DiContainerBeta.search_partners_by_text_use_case])
):
    """ ToDo: DocString """
    query = SearchPartnersByTextQuery(request_params)
    vm = await use_case.execute(query)
    return ResponseOk("'search_partners_by_text', from extended FastAPI!", vm)

@router.delete("/partners/{id}", response_model=Response200Vm[DeletePartnersVm], responses={422:{"model":Response422Vm}})
@inject
async def delete_partner(
    id: int,
    use_case: DeletePartnersUseCase=Depends(Provide[DiContainerBeta.delete_partners_use_case])
):
    """ ToDo: DocString """
    route = DeletePartnerRoute(id=id)
    command = DeletePartnersCommand(route, None)
    vm = await use_case.execute(command)
    return ResponseOk("'delete_partners', from extended FastAPI!", vm)

@router.put("/partners/{id}", response_model=Response200Vm[UpdatePartnerVm], responses={422:{"model":Response422Vm}})
@inject
async def update_partner(
    id: int,
    dto: UpdatePartnerDto=None,
    use_case: UpdatePartnerUseCase=Depends(Provide[DiContainerBeta.update_partner_use_case])
):
    """ ToDo: DocString """
    route = UpdatePartnerRoute(id=id)
    command = UpdatePartnerCommand(route, dto)
    vm = await use_case.execute(command)        
    return ResponseOk("'update_partner', from extended FastAPI!", vm)

@router.get("/partners/{id}", response_model=Response200Vm[GetPartnerByIdVm], responses={422:{"model":Response422Vm}})
@inject
async def get_partner_by_id(
    id: int,
    use_case: GetPartnerByIdUseCase=Depends(Provide[DiContainerBeta.get_partner_by_id_use_case])
):
    """ ToDo: DocString """
    route = GetPartnerByIdRoute(id=id)
    query = GetPartnerByIdQuery(route)
    vm = await use_case.execute(query)
    return ResponseOk("'get_partner_by_id', from extended FastAPI!", vm)

@router.post("/partners/delete", response_model=Response200Vm[DeletePartnersVm], responses={422:{"model":Response422Vm}})
@inject
async def delete_partners(
    dto: DeletePartnersDto=None,
    use_case: DeletePartnersUseCase=Depends(Provide[DiContainerBeta.delete_partners_use_case])
):
    """ ToDo: DocString """
    command = DeletePartnersCommand(None, dto)
    vm = await use_case.execute(command)        
    return ResponseOk("'delete_partners', from extended FastAPI!", vm)

@router.post("/partners/search", response_model=Response200Vm[PaginatedVm[SearchPartnersByObjectVm]], responses={422:{"model":Response422Vm}})
@inject
async def search_partners_by_object(
    dto: SearchPartnersByObjectDto=None,
    use_case: SearchPartnersByObjectUseCase=Depends(Provide[DiContainerBeta.search_partners_by_object])
):
    """ ToDo: DocString """    
    query = SearchPartnersByObjectQuery(dto)
    vm = await use_case.execute(query)
    return ResponseOk("'search_partners_by_object', from extended FastAPI!", vm)



