"""dafiti_challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from core.api.viewsets import ProdutoViewSet, CompareProdutoViewSet, PromocaoLojaViewSet, ComparacaoViewSet, ConcorrenciaLojaViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Compare Preços API",
      default_version='v1',
      description="API que compara preços dos tênis adidas das lojas Dafiti e Zattini",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="nayanna501@gmail.com"),
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet,basename='produtos')
router.register(r'compare-produtos', CompareProdutoViewSet,basename='compare-produtos')
router.register(r'promocao-loja', PromocaoLojaViewSet,basename='promocao-loja')
router.register(r'comparacao', ComparacaoViewSet,basename='comparacao')
router.register(r'concorrencia-loja', ConcorrenciaLojaViewSet,basename='concorrencia-loja')

urlpatterns = [
    path('api/', include(router.urls)),
    path("", include("core.urls")),
    path('admin/', admin.site.urls),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
