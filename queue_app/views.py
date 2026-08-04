from django.shortcuts import render
from notifications.models import Notification
from reports.models import Report

def dashboard(request):

    total_notifications = Notification.objects.count()

    unread_notifications = Notification.objects.filter(status='Unread').count()

    total_reports = Report.objects.count()

    recent_notifications = Notification.objects.order_by('-created_at')[:5]

    context = {
        'total_notifications': total_notifications,
        'unread_notifications': unread_notifications,
        'total_reports': total_reports,
        'recent_notifications': recent_notifications,
    }

    return render(request, 'dashboard/dashboard.html', context)