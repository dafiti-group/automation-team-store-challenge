from .api.viewsets import (UserViewSet, AddressViewSet)
from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'address', AddressViewSet, basename='address')
