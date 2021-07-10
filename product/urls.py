from .api.viewsets import (DepartmentViewSet, CategoryViewSet, BrandViewSet, ProductViewSet, ProductColorViewSet, ProductSizeViewSet, ProductImagesViewSet)
from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='departments')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'brands', BrandViewSet, basename='brands')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'product/colors', ProductColorViewSet, basename='product_colors')
router.register(r'product/sizes', ProductSizeViewSet, basename='product_sizes')
router.register(r'product/images', ProductImagesViewSet, basename='product_images')
