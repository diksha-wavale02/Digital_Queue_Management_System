from django.shortcuts import render


def dashboard(request):
    context = {
        "total_tokens": 156,
        "waiting_tokens": 23,
        "completed_tokens": 121,
        "cancelled_tokens": 12,
    }
    return render(request, "dashboard/dashboard.html", context)


def token_card(request):
    context = {
        "token_no": "A105",
        "service": "General Service",
        "queue_position": 3,
        "estimated_time": "12 Minutes",
    }
    return render(request, "dashboard/token_card.html", context)


def queue_status(request):
    queue = [
        {"counter": "Counter 1", "token": "A102", "status": "Serving"},
        {"counter": "Counter 2", "token": "A105", "status": "Waiting"},
        {"counter": "Counter 3", "token": "A108", "status": "Serving"},
    ]

    return render(request, "dashboard/queue_status.html", {"queue": queue})


def notifications(request):
    notification_list = [
        {"title": "Queue Delay", "status": "Unread"},
        {"title": "Token Called", "status": "Read"},
        {"title": "Appointment Reminder", "status": "Unread"},
        {"title": "Counter Changed", "status": "Read"},
    ]

    return render(
        request,
        "dashboard/notifications.html",
        {"notifications": notification_list},
    )


def token_history(request):
    history = [
        {
            "token": "A101",
            "service": "Hospital OPD",
            "date": "06-08-2026",
            "time": "10:30 AM",
            "status": "Completed",
        },
        {
            "token": "A102",
            "service": "Bank Service",
            "date": "05-08-2026",
            "time": "11:15 AM",
            "status": "Completed",
        },
        {
            "token": "A103",
            "service": "Passport Office",
            "date": "04-08-2026",
            "time": "02:00 PM",
            "status": "Cancelled",
        },
        {
            "token": "A104",
            "service": "Government Office",
            "date": "03-08-2026",
            "time": "12:45 PM",
            "status": "Completed",
        },
    ]

    return render(
        request,
        "dashboard/token_history.html",
        {"history": history},
    )
from django.shortcuts import render

def dashboard(request):

    context = {

        "users":125,
        "services":12,
        "tokens":55,
        "waiting":18,
        "completed":40,
        "cancelled":2,

    }

    return render(request,
                  "dashboard/dashboard.html",
                  context)



def dashboard(request):
    return render(request, "dashboard/dashboard.html")