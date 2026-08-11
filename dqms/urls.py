from django.contrib import admin
from django.urls import path, include
from dashboard.views import logout_view

urlpatterns = [

    path("admin/", admin.site.urls),

    path("", include("dashboard.urls")),

    path("users/", include("users.urls")),

    path("dashboard/", include("dashboard.urls")),

    path("services/", include("services.urls")),

    path("appointments/", include("appointments.urls")),

    path("notifications/", include("notifications.urls")),

    path("reports/", include("reports.urls")),

    path("staff/", include("staff.urls")),

    path("analytics/", include("analytics.urls")),

    path("queue/", include("queue_app.urls")),

    path("logout/", logout_view, name="logout"),
]