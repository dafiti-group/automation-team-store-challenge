from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', product_list.as_view()),
    path('',search, name='search'),
]