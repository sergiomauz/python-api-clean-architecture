from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from di_container_beta import DiContainerBeta
from application.commons.vms import PaginatedVm
from application.use_cases.products.commands.create_product import (
    CreateProductDto, CreateProductCommand, CreateProductUseCase, CreateProductVm
)
from application.use_cases.products.commands.delete_products import (
    DeleteProductRoute, DeleteProductsDto, DeleteProductsCommand, DeleteProductsUseCase, DeleteProductsVm
)
from application.use_cases.products.commands.update_product import (
    UpdateProductRoute,  UpdateProductDto, UpdateProductCommand, UpdateProductUseCase, UpdateProductVm
)
from application.use_cases.products.queries.get_product_by_id import (
    GetProductByIdRoute, GetProductByIdQuery, GetProductByIdUseCase, GetProductByIdVm
)
from application.use_cases.products.queries.search_products_by_text import (
    SearchProductsByTextRequestParams, SearchProductsByTextQuery, SearchProductsByTextUseCase, SearchProductsByTextVm
)
from application.use_cases.products.queries.search_products_by_object import (
    SearchProductsByObjectDto, SearchProductsByObjectQuery, SearchProductsByObjectUseCase, SearchProductsByObjectVm
)
from presentation.app_fastapi.responses import ResponseOk
from presentation.app_fastapi.docs.responses import Response200Vm, Response422Vm, Response409Vm


router = APIRouter(
    prefix="",
    tags=["Products"]
)

@router.post("/products", response_model=Response200Vm[CreateProductVm], responses={422:{"model":Response422Vm}, 409:{"model":Response409Vm}})
@inject
async def create_product(
    dto: CreateProductDto=None,
    use_case: CreateProductUseCase=Depends(Provide[DiContainerBeta.create_product_use_case])
):
    """ ToDo: DocString """
    command = CreateProductCommand(dto)
    vm = await use_case.execute(command)        
    return ResponseOk("'create_product', from extended FastAPI!", vm)

@router.get("/products", response_model=Response200Vm[PaginatedVm[SearchProductsByTextVm]], responses={422:{"model":Response422Vm}})
@inject
async def search_products_by_text(
    request_params: SearchProductsByTextRequestParams=Depends(),
    use_case: SearchProductsByTextUseCase=Depends(Provide[DiContainerBeta.search_products_by_text_use_case])
):
    """ ToDo: DocString """
    query = SearchProductsByTextQuery(request_params)
    vm = await use_case.execute(query)
    return ResponseOk("'search_products_by_text', from extended FastAPI!", vm)

@router.delete("/products/{id}", response_model=Response200Vm[DeleteProductsVm], responses={422:{"model":Response422Vm}})
@inject
async def delete_product(
    id: int,
    use_case: DeleteProductsUseCase=Depends(Provide[DiContainerBeta.delete_products_use_case])
):
    """ ToDo: DocString """
    route = DeleteProductRoute(id=id)
    command = DeleteProductsCommand(route, None)
    vm = await use_case.execute(command)
    return ResponseOk("'delete_products', from extended FastAPI!", vm)

@router.put("/products/{id}", response_model=Response200Vm[UpdateProductVm], responses={422:{"model":Response422Vm}})
@inject
async def update_product(
    id: int,
    dto: UpdateProductDto=None,
    use_case: UpdateProductUseCase=Depends(Provide[DiContainerBeta.update_product_use_case])
):
    """ ToDo: DocString """
    route = UpdateProductRoute(id=id)
    command = UpdateProductCommand(route, dto)
    vm = await use_case.execute(command)        
    return ResponseOk("'update_product', from extended FastAPI!", vm)

@router.get("/products/{id}", response_model=Response200Vm[GetProductByIdVm], responses={422:{"model":Response422Vm}})
@inject
async def get_product_by_id(
    id: int,
    use_case: GetProductByIdUseCase=Depends(Provide[DiContainerBeta.get_product_by_id_use_case])
):
    """ ToDo: DocString """
    route = GetProductByIdRoute(id=id)
    query = GetProductByIdQuery(route)
    vm = await use_case.execute(query)
    return ResponseOk("'get_product_by_id', from extended FastAPI!", vm)

@router.post("/products/delete", response_model=Response200Vm[DeleteProductsVm], responses={422:{"model":Response422Vm}})
@inject
async def delete_products(
    dto: DeleteProductsDto=None,
    use_case: DeleteProductsUseCase=Depends(Provide[DiContainerBeta.delete_products_use_case])
):
    """ ToDo: DocString """
    command = DeleteProductsCommand(None, dto)
    vm = await use_case.execute(command)        
    return ResponseOk("'delete_products', from extended FastAPI!", vm)

@router.post("/products/search", response_model=Response200Vm[PaginatedVm[SearchProductsByObjectVm]], responses={422:{"model":Response422Vm}})
@inject
async def search_products_by_object(
    dto: SearchProductsByObjectDto=None,
    use_case: SearchProductsByObjectUseCase=Depends(Provide[DiContainerBeta.search_products_by_object])
):
    """ ToDo: DocString """    
    query = SearchProductsByObjectQuery(dto)
    vm = await use_case.execute(query)
    return ResponseOk("'search_products_by_object', from extended FastAPI!", vm)



