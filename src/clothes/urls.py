from django.urls import path

from . import views

urlpatterns = [
    path("clothes", views.create_get_delete, name="clothes"),
    path("clothes/<int:foreign_key>/",
         views.operation_by_index,
         name="clothes"),
    path("clothes/by_csv",
         views.FileUploadView.create_by_csv_file,
         name="clothes")
]
