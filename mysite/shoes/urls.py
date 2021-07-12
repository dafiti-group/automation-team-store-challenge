from rest_framework import routers

from .views import ShoesViewSet

shoes_router = routers.DefaultRouter()
shoes_router.register("shoes", viewset=ShoesViewSet, basename="shoes")