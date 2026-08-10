from django.shortcuts import render, redirect, get_object_or_404
from .models import Notification

def dashboard(request):
    unread_count = Notification.objects.filter(status='unread').count()
    return render(request, 'dashboard/dashboard.html', {'unread_count': unread_count})
def notifications(request):  
    notification_list = Notification.objects.all()[:30]
    unread_count = Notification.objects.filter(status='unread').count()
    return render(request, 'notifications/notifications.html', {
        'notifications': notification_list, 
        'unread_count': unread_count
    })

def notification_list(request): # dummy data for testing
    notifications = [
        {'id': 1, 'title': 'Counter 3 is now Free', 'message': 'Counter 3 available', 'created_at': '2 min ago', 'notification_type': 'success', 'status': 'unread'},
        {'id': 2, 'title': 'Token #A105 Completed', 'message': 'Patient visited', 'created_at': '5 min ago', 'notification_type': 'info', 'status': 'read'},
    ]
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

def mark_as_read(request, pk):
    notif = get_object_or_404(Notification, pk=pk)
    notif.status = 'read'
    notif.save()
    return redirect('notification:notifications')

def delete_notification(request, pk):
    notif = get_object_or_404(Notification, pk=pk)
    notif.delete()
    return redirect('notification:notifications')

def create_notification(request):
    # Admin se add hoga, isliye blank rakha
    return render(request, 'notifications/create_notification.html')

# notifications/views.py
def add_notification(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        message = request.POST.get('message')
        Notification.objects.create(title=title, message=message)
        return redirect('notification:notifications')
    return render(request, 'notifications/add_notification.html')