from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("user-dashboard/", views.user_dashboard, name="user_dashboard"),
    path("staff-dashboard/", views.staff_dashboard, name="staff_dashboard"),
    path("token/", views.token_card, name="token_card"),
    path("queue-status/", views.queue_status, name="queue_status"),
    path("notifications/", views.notifications, name="notifications"),
    path("token-history/", views.token_history, name="token_history"),
]