
from .home_routes import blueprint as home
from .categories_routes import blueprint as categories


routes = [
    home,
    categories
]