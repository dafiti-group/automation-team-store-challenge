"""clothing_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


TEMPLATESWAG = get_schema_view(
    openapi.Info(
        title="Clothing Manager",
        default_version="v1",
        description="Documentation to Clothing manager API",
        contact=openapi.Contact(email="arthuralves187@gmail.com"),
        license=openapi.License(name="Open Source"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

BASE_URL = "api/v1/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(BASE_URL, include("src.clothes.urls")),
    #path(BASE_URL, include("src.clothing_type.urls")),
    path(BASE_URL, include("src.colors.urls")),
    path(BASE_URL, include("src.promotional_campaigns.urls")),
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        TEMPLATESWAG.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(
        "{}{}/".format(BASE_URL, "swagger"),
        TEMPLATESWAG.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$",
        TEMPLATESWAG.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
