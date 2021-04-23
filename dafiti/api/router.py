from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('marcas', views.MarcaViewSet)
router.register('produtos', views.ProdutoViewSet)

api_urlpatterns = router.urls
