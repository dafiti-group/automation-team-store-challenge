from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list.as_view()),
]