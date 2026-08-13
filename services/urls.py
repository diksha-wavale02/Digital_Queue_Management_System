from django.urls import path
from . import views

urlpatterns = [

    path(
        "add/",
        views.add_service,
        name="add_service"
    ),

    path(
        "view/",
        views.view_service,
        name="view_service"
    ),

    path(
        "update/<int:id>/",
        views.update_service,
        name="update_service"
    ),

    path(
        "delete/<int:id>/",
        views.delete_service,
        name="delete_service"
    ),

]