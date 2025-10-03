from sqlalchemy.orm import sessionmaker
from dependency_injector import containers, providers
from infrastructure.persistence import  get_session_by_context, create_sqlalchemy_engine, DbTransactionsManagerAdapter
from infrastructure.persistence.repositories.bases import BaseWithIdRepositoryAdapter


class DiContainerAlpha(containers.DeclarativeContainer):
    config = providers.Configuration()
    
    # DB Session
    engine = providers.Singleton(
        create_sqlalchemy_engine,
        connection_string=config.infrastructure.persistence.connection_string
    )
    session_factory = providers.Singleton(
        sessionmaker,
        bind=engine,
        autocommit=False,
        autoflush=False
    )
    db_session = providers.Resource(
        get_session_by_context,
        session_factory=session_factory
    )

    # DB transactions manager
    db_transactions_manager = providers.Factory(DbTransactionsManagerAdapter,
                                                db_session=db_session)
        
    # Repositories
        
    # Use cases