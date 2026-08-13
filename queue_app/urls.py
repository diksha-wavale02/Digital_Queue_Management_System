from django.urls import path
from . import views

urlpatterns = [
    path(
        'live/<int:appointment_id>/',
        views.live_queue,
        name='live_queue'
    ),
    path(
        "display-board/",
        views.display_board,
        name="display_board"
    ),
    path(
    "call-next/",
    views.call_next,
    name="call_next"
    ),

    path(
        'staff-queue/',
        views.staff_queue,
        name='staff_queue'
    ),
       path(
        "search-token/",
        views.search_token,
        name="search_token"
    ),
    path(
    "staff-dashboard/",
    views.staff_dashboard,
    name="staff_dashboard"
    ),
    
]