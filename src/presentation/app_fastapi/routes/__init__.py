
from fastapi import APIRouter
from .categories_routes import router as categories
from .products_routes import router as products
from .partners_routes import router as partners
from .movements_routes import router as movements

router = APIRouter()
router.include_router(categories)
router.include_router(products)
router.include_router(partners)
router.include_router(movements)