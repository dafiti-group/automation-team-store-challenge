from django.urls import path
from . import views


app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('feminine_shoes/', views.feminine_shoes, name='feminine_shoes'),
    path('masculine_shoes/', views.masculine_shoes, name='masculine_shoes'),
    path('<int:id>/', views.shoes_detail, name='shoes_detail'),
    path('new/', views.ShoeFormView.as_view(), name='shoe_form'),
    path('<int:id>/update/', views.ShoeUpdateView.as_view(), name='update_shoes'),
    path('<int:id>/delete/', views.ShoeDeleteView.as_view(), name='delete_shoes'),
]
