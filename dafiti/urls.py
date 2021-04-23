from django.contrib import admin
from django.urls import path, include

from dafiti.api.router import api_urlpatterns as api_v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1)),
]
