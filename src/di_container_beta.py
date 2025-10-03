from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector import containers, providers
from infrastructure.persistence import (
    get_async_session_by_context, create_sqlalchemy_engine_async, DbTransactionsManagerAdapter
)
from infrastructure.persistence.repositories import (
    CategoriesRepositoryAdapter, ProductsRepositoryAdapter, PartnersRepositoryAdapter, MovementsRepositoryAdapter
)
from application.use_cases import (
    CreateCategoryUseCase, DeleteCategoriesUseCase, UpdateCategoryUseCase,
    GetCategoryByIdUseCase, SearchCategoriesByTextUseCase, SearchCategoriesByObjectUseCase,
    CreateProductUseCase, DeleteProductsUseCase, UpdateProductUseCase,
    GetProductByIdUseCase, SearchProductsByTextUseCase, SearchProductsByObjectUseCase,        
    CreatePartnerUseCase, DeletePartnersUseCase, UpdatePartnerUseCase,
    GetPartnerByIdUseCase, SearchPartnersByTextUseCase, SearchPartnersByObjectUseCase,    
    CreateMovementUseCase, DeleteMovementsUseCase,
    GetMovementByIdUseCase, SearchMovementsByTextUseCase, SearchMovementsByObjectUseCase
)


class DiContainerBeta(containers.DeclarativeContainer):
    config = providers.Configuration()
    
    # DB Session
    engine_async = providers.Singleton(
        create_sqlalchemy_engine_async,
        connection_string=config.infrastructure.persistence.connection_string
    )    
    session_factory_async = providers.Singleton(
        sessionmaker,
        bind=engine_async,
        expire_on_commit=False,
        class_=AsyncSession,
        autocommit=False,
        autoflush=False
    )    
    db_session_async = providers.Resource(
        get_async_session_by_context,
        session_factory=session_factory_async
    )
        
    # DB transactions manager
    db_transactions_manager = providers.Factory(DbTransactionsManagerAdapter,
                                                db_session=db_session_async)
    
    # Repositories and Use cases
    categories_repository = providers.Factory(CategoriesRepositoryAdapter,
                                                db_session=db_session_async)  
    create_category_use_case = providers.Factory(CreateCategoryUseCase,
                                                    categories_repository=categories_repository)
    delete_categories_use_case = providers.Factory(DeleteCategoriesUseCase,
                                                    categories_repository=categories_repository)
    update_category_use_case = providers.Factory(UpdateCategoryUseCase,
                                                    categories_repository=categories_repository)
    get_category_by_id_use_case = providers.Factory(GetCategoryByIdUseCase,
                                                    categories_repository=categories_repository)
    search_categories_by_text_use_case = providers.Factory(SearchCategoriesByTextUseCase,
                                                    categories_repository=categories_repository)
    search_categories_by_object = providers.Factory(SearchCategoriesByObjectUseCase,
                                                    categories_repository=categories_repository)
        
    products_repository = providers.Factory(ProductsRepositoryAdapter,
                                                db_session=db_session_async)  
    create_product_use_case = providers.Factory(CreateProductUseCase,
                                                    products_repository=products_repository,
                                                    categories_repository=categories_repository)
    delete_products_use_case = providers.Factory(DeleteProductsUseCase,
                                                    products_repository=products_repository)
    update_product_use_case = providers.Factory(UpdateProductUseCase,
                                                    products_repository=products_repository,
                                                    categories_repository=categories_repository)
    get_product_by_id_use_case = providers.Factory(GetProductByIdUseCase,
                                                    products_repository=products_repository,
                                                    )
    search_products_by_text_use_case = providers.Factory(SearchProductsByTextUseCase,
                                                    products_repository=products_repository)
    search_products_by_object = providers.Factory(SearchProductsByObjectUseCase,
                                                    products_repository=products_repository)    
        
    partners_repository = providers.Factory(PartnersRepositoryAdapter,
                                                db_session=db_session_async)  
    create_partner_use_case = providers.Factory(CreatePartnerUseCase,
                                                    partners_repository=partners_repository)
    delete_partners_use_case = providers.Factory(DeletePartnersUseCase,
                                                    partners_repository=partners_repository)
    update_partner_use_case = providers.Factory(UpdatePartnerUseCase,
                                                    partners_repository=partners_repository)
    get_partner_by_id_use_case = providers.Factory(GetPartnerByIdUseCase,
                                                    partners_repository=partners_repository)
    search_partners_by_text_use_case = providers.Factory(SearchPartnersByTextUseCase,
                                                    partners_repository=partners_repository)
    search_partners_by_object = providers.Factory(SearchPartnersByObjectUseCase,
                                                    partners_repository=partners_repository)        
        
    movements_repository = providers.Factory(MovementsRepositoryAdapter,
                                                db_session=db_session_async)                  
    create_movement_use_case = providers.Factory(CreateMovementUseCase,
                                                    movements_repository=movements_repository,
                                                    products_repository=products_repository,
                                                    partners_repository=partners_repository)
    delete_movements_use_case = providers.Factory(DeleteMovementsUseCase,
                                                    movements_repository=movements_repository)
    get_movement_by_id_use_case = providers.Factory(GetMovementByIdUseCase,
                                                    movements_repository=movements_repository,
                                                    products_repository=products_repository,
                                                    partners_repository=partners_repository)
    search_movements_by_text_use_case = providers.Factory(SearchMovementsByTextUseCase,
                                                    movements_repository=movements_repository)
    search_movements_by_object = providers.Factory(SearchMovementsByObjectUseCase,
                                                    movements_repository=movements_repository)
