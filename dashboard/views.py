from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test

from notifications.models import Notification
from queue_app.models import Token


# =========================================================
# NORMAL USER DASHBOARD
# =========================================================

@login_required
def dashboard(request):

    unread_count = Notification.objects.filter(
        status="unread"
    ).count()

    context = {
        "users": 125,
        "services": 12,
        "tokens": 55,
        "waiting": 18,
        "completed": 40,
        "cancelled": 2,
        "unread_count": unread_count,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )


# =========================================================
# TOKEN CARD
# =========================================================

@login_required
def token_card(request):

    token = Token.objects.filter(
        status="pending"
    ).order_by("-created_at").first()

    unread_count = Notification.objects.filter(
        status="unread"
    ).count()

    return render(
        request,
        "dashboard/token_card.html",
        {
            "token": token,
            "unread_count": unread_count,
        }
    )


# =========================================================
# QUEUE STATUS
# =========================================================

@login_required
def queue_status(request):

    queue = [
        {
            "counter": "Counter 1",
            "token": "A102",
            "status": "Serving",
        },
        {
            "counter": "Counter 2",
            "token": "A105",
            "status": "Waiting",
        },
        {
            "counter": "Counter 3",
            "token": "A108",
            "status": "Serving",
        },
    ]

    return render(
        request,
        "dashboard/queue_status.html",
        {
            "queue": queue
        }
    )


# =========================================================
# NOTIFICATIONS
# =========================================================

@login_required
def notifications(request):

    notification_list = Notification.objects.all().order_by(
        "-created_at"
    )[:30]

    unread_count = Notification.objects.filter(
        status="unread"
    ).count()

    return render(
        request,
        "notifications/notifications.html",
        {
            "notifications": notification_list,
            "unread_count": unread_count,
        }
    )


# =========================================================
# TOKEN HISTORY
# =========================================================

@login_required
def token_history(request):

    tokens = Token.objects.all().order_by(
        "-created_at"
    )

    query = request.GET.get("q")

    if query:
        tokens = tokens.filter(
            token_number__icontains=query
        )

    unread_count = Notification.objects.filter(
        status="unread"
    ).count()

    return render(
        request,
        "dashboard/token_history.html",
        {
            "tokens": tokens,
            "unread_count": unread_count,
        }
    )


# =========================================================
# LOGOUT
# =========================================================

@login_required
def logout_view(request):

    logout(request)

    return redirect("login")


# =========================================================
# ADMIN CHECK
# =========================================================

def admin_check(user):

    return (
        user.is_authenticated
        and user.is_superuser
    )


# =========================================================
# ADMIN DASHBOARD
# =========================================================

@user_passes_test(admin_check)
def admin_dashboard(request):

    return render(
        request,
        "dashboard/admin_dashboard.html"
    )


# =========================================================
# USER DASHBOARD
# =========================================================

@login_required
def user_dashboard(request):

    return render(
        request,
        "dashboard/user_dashboard.html"
    )


# =========================================================
# STAFF DASHBOARD
# =========================================================

@login_required
def staff_dashboard(request):

    return render(
        request,
        "dashboard/staff_dashboard.html"
    )