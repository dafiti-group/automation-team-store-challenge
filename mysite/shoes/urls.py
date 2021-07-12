from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtaionPairView, TokenRefreshView)
from .views import ShoesViewSet

shoes_router = routers.DefaultRouter()
shoes_router.register("shoes", viewset=ShoesViewSet, basename="shoes")

from django.urls import path

urlpatterns = [
    path('posts/', ShoesView.as_view(), name='posts_view')
]