from django.urls import path
from . import views


urlpatterns = [

    path(
        'book/',
        views.book_appointment,
        name='book_appointment'
    ),

    path(
        'view/',
        views.view_appointment,
        name='view_appointment'
    ),

    path(
        'update/<int:id>/',
        views.update_appointment,
        name='update_appointment'
    ),

    path(
        'cancel/<int:id>/',
        views.cancel_appointment,
        name='cancel_appointment'
    ),

    path(
        'history/',
        views.appointment_history,
        name='appointment_history'
    ),
      path(
        "get-services/",
        views.get_services_by_category,
        name="get_services_by_category"
    ),
    path(
    "get-locations/",
    views.get_locations_by_category,
    name="get_locations_by_category"
    ),
    path(
    "confirmation/<int:appointment_id>/",
    views.appointment_confirmation,
    name="appointment_confirmation"
    ),
    path(
    'get-services-by-category/',
    views.get_services_by_category,
    name='get_services_by_category'
),
path(
    'user-cancel/<int:id>/',
    views.user_cancel_appointment,
    name='user_cancel_appointment'
),
]