from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate
from tokens.models import Token


def analytics(request):

    daily_tokens = (
        Token.objects
        .annotate(day=TruncDate('created_at'))
        .values('day')
        .annotate(total=Count('id'))
        .order_by('day')
    )

    return render(
        request,
        'analytics/analytics.html',
        {
            'daily_tokens': daily_tokens
        }
    )