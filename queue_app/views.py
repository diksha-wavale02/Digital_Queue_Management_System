from django.shortcuts import render, get_object_or_404, redirect
from .models import Queue

# =========================================================
# STAFF - DASHBOARD
# =========================================================

def staff_dashboard(request):
    return render(
        request,
        "staff/staff_dashboard.html"
    )

# =========================================================
# CUSTOMER - LIVE QUEUE
# =========================================================

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
    if your_queue.status == 'Waiting':
            progress = 0  

    elif your_queue.status == 'Serving':
            progress = 50

    elif your_queue.status == 'Completed':
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


# =========================================================
# STAFF - DISPLAY BOARD
# =========================================================

def display_board(request):

    location_id = request.GET.get('location_id')
    service_id = request.GET.get('service_id')

    current_queue = None
    next_tokens = []

    # Only search when location and service are selected
    if location_id and service_id:

        # -----------------------------------------
        # CURRENTLY SERVING
        # -----------------------------------------

        current_queue = Queue.objects.filter(
            status='Serving',
            appointment__location_id=location_id,
            appointment__service_id=service_id
        ).order_by(
            'token_number'
        ).first()

        # -----------------------------------------
        # WAITING TOKENS
        # -----------------------------------------

        waiting_queue = Queue.objects.filter(
            status='Waiting',
            appointment__location_id=location_id,
            appointment__service_id=service_id
        ).order_by(
            'token_number'
        )

        # Show next 5 tokens
        next_tokens = waiting_queue[:5]

    return render(
        request,
        'queue/display_board.html',
        {
            'current_queue': current_queue,
            'next_tokens': next_tokens,
            'location_id': location_id,
            'service_id': service_id,
        }
    )

# =========================================================
# STAFF - QUEUE PAGE
# =========================================================

def staff_queue(request):

    location_id = request.GET.get('location_id')
    service_id = request.GET.get('service_id')

    current_queue = None
    next_tokens = []

    if location_id and service_id:

        # Currently serving
        current_queue = Queue.objects.filter(
            status='Serving',
            appointment__location_id=location_id,
            appointment__service_id=service_id
        ).order_by(
            'token_number'
        ).first()

        # Waiting tokens
        next_tokens = Queue.objects.filter(
            status='Waiting',
            appointment__location_id=location_id,
            appointment__service_id=service_id
        ).order_by(
            'token_number'
        )[:5]

    return render(
        request,
        'queue/staff_queue.html',
        {
            'current_queue': current_queue,
            'next_tokens': next_tokens,
            'location_id': location_id,
            'service_id': service_id,
        }
    )




# =========================================================
# STAFF - CALL NEXT
# =========================================================
def call_next(request):

    if request.method == 'POST':

        location_id = request.POST.get('location_id')
        service_id = request.POST.get('service_id')

        if location_id and service_id:

            # Complete current token
            Queue.objects.filter(
                status='Serving',
                appointment__location_id=location_id,
                appointment__service_id=service_id
            ).update(
                status='Completed'
            )

            # Find next waiting token
            next_queue = Queue.objects.filter(
                status='Waiting',
                appointment__location_id=location_id,
                appointment__service_id=service_id
            ).order_by(
                'token_number'
            ).first()

            # Make next token Serving
            if next_queue:
                next_queue.status = 'Serving'
                next_queue.save()

        return redirect(
            f'/queue/display-board/?location_id={location_id}&service_id={service_id}'
        )

    return redirect('/queue/display-board/')

# =========================================================
# STAFF - SEARCH QUEUE
# =========================================================def search_queue(request):
def search_token(request):

    queue = None
    searched_token = ""

    if request.method == "POST":

        searched_token = request.POST.get(
            "token_number",
            ""
        ).strip()

        # Convert Q001 → 1
        token = searched_token.upper().replace("Q", "")

        if token.isdigit():

            queue = Queue.objects.filter(
                token_number=int(token)
            ).select_related(
                "appointment",
                "appointment__service",
                "appointment__location"
            ).first()

    return render(
        request,
        "queue/search_token.html",
        {
            "queue": queue,
            "searched_token": searched_token,
        }
    )