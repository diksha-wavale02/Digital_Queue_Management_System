from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .models import Appointment
from .forms import AppointmentForm

from queue_app.models import Queue
from services.models import Service
from locations.models import Location


# =========================================================
# USER - BOOK APPOINTMENT
# =========================================================

def book_appointment(request):

    if request.method == 'POST':

        form = AppointmentForm(request.POST)

        if form.is_valid():

            # Save appointment
            appointment = form.save()

            # -----------------------------------------
            # FIND SAME LOCATION + SAME SERVICE
            # -----------------------------------------

            same_queue = Queue.objects.filter(
                appointment__location=appointment.location,
                appointment__service=appointment.service
            )

            # -----------------------------------------
            # GENERATE NEXT TOKEN
            # -----------------------------------------

            last_queue = same_queue.order_by(
                '-token_number'
            ).first()

            if last_queue:
                next_token = last_queue.token_number + 1
            else:
                next_token = 1

            # -----------------------------------------
            # CREATE QUEUE
            # -----------------------------------------

            Queue.objects.create(
                appointment=appointment,
                token_number=next_token,
                status='Waiting'
            )

            # -----------------------------------------
            # CONFIRMATION PAGE
            # -----------------------------------------

            return redirect(
                'appointment_confirmation',
                  appointment_id=appointment.id
            )

    else:

        form = AppointmentForm()

    return render(
        request,
        'appointments/book_appointment.html',
        {
            'form': form
        }
    )


# =========================================================
# USER - APPOINTMENT CONFIRMATION
# =========================================================

def appointment_confirmation(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )

    queue = get_object_or_404(
        Queue,
        appointment=appointment
    )

    return render(
        request,
        'appointments/appointment_confirmation.html',
        {
            'appointment': appointment,
            'queue': queue,
        }
    )



# =========================================================
# STAFF - VIEW APPOINTMENTS
# =========================================================

def view_appointment(request):

    appointments = Appointment.objects.filter(
        status='Booked'
    ).order_by(
        'appointment_date',
        'appointment_time'
    )

    return render(
        request,
        'appointments/view_appointment.html',
        {
            'appointments': appointments
        }
    )


# =========================================================
# STAFF - UPDATE APPOINTMENT
# =========================================================

def update_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    if request.method == 'POST':

        form = AppointmentForm(
            request.POST,
            instance=appointment
        )

        if form.is_valid():

            form.save()

            return redirect(
                'view_appointment'
            )

    else:

        form = AppointmentForm(
            instance=appointment
        )

    return render(
        request,
        'appointments/update_appointment.html',
        {
            'form': form,
            'appointment': appointment,
        }
    )


# =========================================================
# STAFF - CANCEL APPOINTMENT
# =========================================================

def cancel_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    appointment.status = 'Cancelled'
    appointment.save()

    # Also update queue status
    Queue.objects.filter(
        appointment=appointment
    ).update(
        status='Cancelled'
    )

    return redirect(
        'appointment_history'
    )


# =========================================================
# STAFF - APPOINTMENT HISTORY
# =========================================================

def appointment_history(request):

    appointments = Appointment.objects.all().order_by(
        '-appointment_date',
        '-appointment_time'
    )

    return render(
        request,
        'appointments/appointment_history.html',
        {
            'appointments': appointments
        }
    )


# =========================================================
# GET SERVICES BY CATEGORY
# =========================================================

def get_services_by_category(request):

    category_id = request.GET.get('category_id')

    services = Service.objects.filter(
        category_id=category_id
    )

    data = []

    for service in services:

        data.append({
            'id': service.id,
            'name': service.name
        })

    return JsonResponse({
        'services': data
    })
# =========================================================
# GET LOCATION BY CATEGORY
# =========================================================
def get_locations_by_category(request):

    category_id = request.GET.get('category_id')

    locations = Location.objects.filter(
        category_id=category_id
    )

    data = []

    for location in locations:
        data.append({
            'id': location.id,
            'name': location.name,
            'address': location.address,
            'city': location.city,
        })

    return JsonResponse({
        'locations': data
    })

        
# =========================================================
# LIVE QUEUE
# =========================================================
def live_queue(request, appointment_id):

    your_queue = get_object_or_404(
        Queue,
        appointment_id=appointment_id
    )

    appointment = your_queue.appointment

    same_queue = Queue.objects.filter(
        appointment__location=appointment.location,
        appointment__service=appointment.service
    )

    current_serving = same_queue.filter(
        status='Serving'
    ).order_by(
        'token_number'
    ).first()

    people_ahead = same_queue.filter(
        status='Waiting',
        token_number__lt=your_queue.token_number
    ).count()

    waiting_time = people_ahead * 5

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