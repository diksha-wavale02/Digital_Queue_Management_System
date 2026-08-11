from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("dashboard/", include("dashboard.urls")),

    # other apps
    path("appointments/", include("appointments.urls")),
    path("services/", include("services.urls")),
    path("queue/", include("queue_app.urls")),
    path("notifications/", include("notifications.urls")),
    path("staff/", include("staff.urls")),
    path("reports/", include("reports.urls")),
    path("users/", include("users.urls")),
    path("analytics/", include("analytics.urls")),
]