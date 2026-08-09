from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate
from tokens.models import Token


def analytics(request):

    total_tokens = Token.objects.count()

    completed_tokens = Token.objects.filter(
        status="Completed"
    ).count()

    waiting_tokens = Token.objects.filter(
        status="Waiting"
    ).count()

    cancelled_tokens = Token.objects.filter(
        status="Cancelled"
    ).count()

    # Daily tokens
    daily_tokens = (
        Token.objects
        .annotate(day=TruncDate("created_at"))
        .values("day")
        .annotate(total=Count("id"))
        .order_by("day")
    )

    # Service-wise tokens
    service_tokens = (
        Token.objects
        .values("service")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    return render(request, "analytics/analytics.html", {
        "total_tokens": total_tokens,
        "completed_tokens": completed_tokens,
        "waiting_tokens": waiting_tokens,
        "cancelled_tokens": cancelled_tokens,
        "daily_tokens": daily_tokens,
        "service_tokens": service_tokens,
    })