from django.shortcuts import render, redirect
from .models import Notification
from .forms import NotificationForm
from django.shortcuts import get_object_or_404




def notification_list(request):

    notifications = Notification.objects.all()

    return render(
        request,
        'notifications/notification_list.html',
        {'notifications': notifications}
    )


def add_notification(request):

    if request.method == 'POST':

        form = NotificationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('notification_list')

    else:

        form = NotificationForm()

    return render(
        request,
        'notifications/add_notification.html',
        {'form': form}
    )

def delete_notification(request, id):

    notification = get_object_or_404(Notification, id=id)

    if request.method == 'POST':
        notification.delete()
        return redirect('notification_list')

    return render(
        request,
        'notifications/delete_notification.html',
        {'notification': notification}
    )


def update_notification(request, id):

    notification = get_object_or_404(Notification, id=id)

    if request.method == "POST":
        form = NotificationForm(request.POST, instance=notification)

        if form.is_valid():
            form.save()
            return redirect('notification_list')

    else:
        form = NotificationForm(instance=notification)

    return render(
        request,
        'notifications/update_notification.html',
        {'form': form}
    )