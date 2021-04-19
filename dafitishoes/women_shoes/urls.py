from django.urls import path

from . import views

app_name = "women_shoes"

urlpatterns = [
    path('', views.index, name='index'),
    # path('women_shoes_list/<int:id>/', views.women_shoes_list, name='women_shoes_list'),
]