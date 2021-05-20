from ninja import NinjaAPI

from backend.product.api import router as product_router
from backend.shopping.api import router as shopping_router

api = NinjaAPI()

api.add_router("/product/", product_router)
api.add_router("/shopping/", shopping_router)
