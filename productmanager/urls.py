from django.contrib import admin
from django.urls import path
from products import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/products/$', views.products_list),
    url(r'^api/products/(?P<pk>[0-9]+)$', views.products_detail),
    url(r'^api/categories/$', views.categories_list),
    url(r'^api/brands/$', views.brands_list),
]