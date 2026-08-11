from django.shortcuts import render, get_object_or_404, redirect
from .models import Queue


def live_queue(request, appointment_id):

    your_queue = get_object_or_404(
        Queue,
        appointment_id=appointment_id
    )

    appointment = your_queue.appointment

    # Same location + same service
    same_queue = Queue.objects.filter(
        appointment__location=appointment.location,
        appointment__service=appointment.service
    )

    # Currently serving
    current_serving = same_queue.filter(
        status='Serving'
    ).order_by(
        'token_number'
    ).first()

    # People ahead
    people_ahead = same_queue.filter(
        status='Waiting',
        token_number__lt=your_queue.token_number
    ).count()

    # Waiting time
    waiting_time = people_ahead * 5

    # Progress
    if your_queue.status == 'Completed':

        progress = 100

    elif your_queue.status == 'Serving':

        progress = 100

    else:

        progress = 0

    return render(
        request,
        'appointments/live_queue.html',
        {
            'your_queue': your_queue,
            'current_serving': current_serving,
            'people_ahead': people_ahead,
            'waiting_time': waiting_time,
            'progress': progress,
        }
    )


def display_board(request):

    # Get currently serving token
    current_queue = Queue.objects.filter(
        status="Serving"
    ).order_by("token_number").first()

    # Get waiting tokens
    waiting_queue = Queue.objects.filter(
        status="Waiting"
    ).order_by("token_number")

    # Get next 5 tokens
    next_tokens = waiting_queue[:5]

    return render(
        request,
        "queue/display_board.html",
        {
            "current_queue": current_queue,
            "next_tokens": next_tokens,
        }
    )

    return render(
        request,
        "queue/display_board.html",
        context
    )




def call_next(request):

    # Complete currently serving token
    Queue.objects.filter(
        status="Serving"
    ).update(
        status="Completed"
    )

    # Find next waiting token
    next_queue = Queue.objects.filter(
        status="Waiting"
    ).order_by("token_number").first()

    if next_queue:
        next_queue.status = "Serving"
        next_queue.save()

    return redirect("display_board")