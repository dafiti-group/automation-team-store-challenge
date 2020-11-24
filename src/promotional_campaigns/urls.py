from django.urls import path

from . import views

urlpatterns = [
    path("promotional_campaign",
         views.create_get_delete,
         name="promotional_campaign"),
    path("promotional_campaign/<int:foreign_key>/",
         views.operation_by_index,
         name="promotional_campaign")
]
