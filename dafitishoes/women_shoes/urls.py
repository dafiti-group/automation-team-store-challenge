from django.urls import include, path
from rest_framework import routers
from . import views

app_name = "women_shoes"

router = routers.DefaultRouter()
# router.register(r'women-shoes', views.WomenShoesViewSet)

urlpatterns = [
    path('women_shoes/', views.women_shoes_list),
    path('women_shoes/<int:pk>/', views.women_shoes_detail)
]
