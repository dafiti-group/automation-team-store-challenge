from django.urls import path

from . import views

urlpatterns = [
    path("color", views.create_get_delete, name="color"),
    path("color/<int:foreign_key>/", views.operation_by_index, name="color")
]
