from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from di_container_beta import DiContainerBeta
from application.commons.vms import PaginatedVm
from application.use_cases.categories.commands.create_category import (
    CreateCategoryDto, CreateCategoryCommand, CreateCategoryUseCase, CreateCategoryVm
)
from application.use_cases.categories.commands.delete_categories import (
    DeleteCategoryRoute, DeleteCategoriesDto, DeleteCategoriesCommand, DeleteCategoriesUseCase, DeleteCategoriesVm
)
from application.use_cases.categories.commands.update_category import (
    UpdateCategoryRoute,  UpdateCategoryDto, UpdateCategoryCommand, UpdateCategoryUseCase, UpdateCategoryVm
)
from application.use_cases.categories.queries.get_category_by_id import (
    GetCategoryByIdRoute, GetCategoryByIdQuery, GetCategoryByIdUseCase, GetCategoryByIdVm
)
from application.use_cases.categories.queries.search_categories_by_text import (
    SearchCategoriesByTextRequestParams, SearchCategoriesByTextQuery, SearchCategoriesByTextUseCase, SearchCategoriesByTextVm
)
from application.use_cases.categories.queries.search_categories_by_object import (
    SearchCategoriesByObjectDto, SearchCategoriesByObjectQuery, SearchCategoriesByObjectUseCase, SearchCategoriesByObjectVm
)
from presentation.app_fastapi.responses import ResponseOk
from presentation.app_fastapi.docs.responses import Response200Vm, Response422Vm, Response409Vm


router = APIRouter(
    prefix="",
    tags=["Categories"]
)

@router.post("/categories", response_model=Response200Vm[CreateCategoryVm], responses={422:{"model":Response422Vm}, 409:{"model":Response409Vm}})
@inject
async def create_category(
    dto: CreateCategoryDto=None,
    use_case: CreateCategoryUseCase=Depends(Provide[DiContainerBeta.create_category_use_case])
):
    """ ToDo: DocString """
    command = CreateCategoryCommand(dto)
    vm = await use_case.execute(command)        
    return ResponseOk("'create_category', from extended FastAPI!", vm)

@router.get("/categories", response_model=Response200Vm[PaginatedVm[SearchCategoriesByTextVm]], responses={422:{"model":Response422Vm}})
@inject
async def search_categories_by_text(
    request_params: SearchCategoriesByTextRequestParams=Depends(),
    use_case: SearchCategoriesByTextUseCase=Depends(Provide[DiContainerBeta.search_categories_by_text_use_case])
):
    """ ToDo: DocString """
    query = SearchCategoriesByTextQuery(request_params)
    vm = await use_case.execute(query)
    return ResponseOk("'search_categories_by_text', from extended FastAPI!", vm)

@router.delete("/categories/{id}", response_model=Response200Vm[DeleteCategoriesVm], responses={422:{"model":Response422Vm}})
@inject
async def delete_category(
    id: int,
    use_case: DeleteCategoriesUseCase=Depends(Provide[DiContainerBeta.delete_categories_use_case])
):
    """ ToDo: DocString """
    route = DeleteCategoryRoute(id=id)
    command = DeleteCategoriesCommand(route, None)
    vm = await use_case.execute(command)
    return ResponseOk("'delete_categories', from extended FastAPI!", vm)

@router.put("/categories/{id}", response_model=Response200Vm[UpdateCategoryVm], responses={422:{"model":Response422Vm}})
@inject
async def update_category(
    id: int,
    dto: UpdateCategoryDto=None,
    use_case: UpdateCategoryUseCase=Depends(Provide[DiContainerBeta.update_category_use_case])
):
    """ ToDo: DocString """
    route = UpdateCategoryRoute(id=id)
    command = UpdateCategoryCommand(route, dto)
    vm = await use_case.execute(command)        
    return ResponseOk("'update_category', from extended FastAPI!", vm)

@router.get("/categories/{id}", response_model=Response200Vm[GetCategoryByIdVm], responses={422:{"model":Response422Vm}})
@inject
async def get_category_by_id(
    id: int,
    use_case: GetCategoryByIdUseCase=Depends(Provide[DiContainerBeta.get_category_by_id_use_case])
):
    """ ToDo: DocString """
    route = GetCategoryByIdRoute(id=id)
    query = GetCategoryByIdQuery(route)
    vm = await use_case.execute(query)
    return ResponseOk("'get_category_by_id', from extended FastAPI!", vm)

@router.post("/categories/delete", response_model=Response200Vm[DeleteCategoriesVm], responses={422:{"model":Response422Vm}})
@inject
async def delete_categories(
    dto: DeleteCategoriesDto=None,
    use_case: DeleteCategoriesUseCase=Depends(Provide[DiContainerBeta.delete_categories_use_case])
):
    """ ToDo: DocString """
    command = DeleteCategoriesCommand(None, dto)
    vm = await use_case.execute(command)        
    return ResponseOk("'delete_categories', from extended FastAPI!", vm)

@router.post("/categories/search", response_model=Response200Vm[PaginatedVm[SearchCategoriesByObjectVm]], responses={422:{"model":Response422Vm}})
@inject
async def search_categories_by_object(
    dto: SearchCategoriesByObjectDto=None,
    use_case: SearchCategoriesByObjectUseCase=Depends(Provide[DiContainerBeta.search_categories_by_object])
):
    """ ToDo: DocString """    
    query = SearchCategoriesByObjectQuery(dto)
    vm = await use_case.execute(query)
    return ResponseOk("'search_categories_by_object', from extended FastAPI!", vm)



