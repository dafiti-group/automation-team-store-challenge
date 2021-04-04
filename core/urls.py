from django.urls import path
from .views import produtos, home, produto_compare, compare,comparacao, concorrencia, remove

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("produtos/", produtos, name="produtos"),
    path("compare-produto/<int:id>/", produto_compare, name="produto_compare"),
    path("compare/", compare, name="compare"),
    path("comparacao/", comparacao, name="comparacao"),
    path("concorrencia/", concorrencia, name="concorrencia"),
    path("remove/<int:id>/", remove, name="remove"),
    
]