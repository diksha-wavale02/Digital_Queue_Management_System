from django.shortcuts import render, redirect

def notification_list(request):
    notifications = [
        {'id': 1, 'title': 'Counter 3 is now Free', 'time': '2 min ago', 'type': 'success'},
        {'id': 2, 'title': 'Token #A105 Completed', 'time': '5 min ago', 'type': 'info'},
        {'id': 3, 'title': 'Staff Raj marked as Inactive', 'time': '10 min ago', 'type': 'warning'},
    ]
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

def add_notification(request):
    return redirect('notification_list')

def create_notification(request):
    return render(request, 'notifications/create_notification.html')

def update_notification(request, pk):
    return render(request, 'notifications/update_notification.html', {'pk': pk})

def delete_notification(request, pk):
    return redirect('notification_list')