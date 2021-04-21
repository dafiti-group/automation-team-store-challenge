from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.WomenShoesList.as_view()),
    path('detail/<int:pk>/', views.WomenShoesDetail.as_view()),
]
