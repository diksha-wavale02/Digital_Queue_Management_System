from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Staff
from .forms import StaffForm

def dashboard(request):
    recent_notifications = [
        {'title': 'Counter 3 is now Free', 'time': '2 min ago', 'type': 'success'},
        {'title': 'Token #A105 Completed', 'time': '5 min ago', 'type': 'info'},
        {'title': 'Staff Raj marked as Inactive', 'time': '10 min ago', 'type': 'warning'},
    ]

    context = {
        'total_tokens': 25,
        'waiting_tokens': 8,
        'completed_tokens': 142,
        'active_staff': Staff.objects.filter(status='Active').count(),
        'recent_notifications': recent_notifications  # dashboard ko connect kar diya
    }
    return render(request, 'queue_app/dashboard.html', context)

def queue_management(request):
    staff = Staff.objects.filter(status='Active')
    return render(request, 'queue_app/queue_management.html', {'staff_list': staff})

def service_management(request):
    services = [
        {'name': 'Token Issue', 'counter': 'C1', 'avg_time': '2 min'},
        {'name': 'Document Verification', 'counter': 'C2', 'avg_time': '5 min'},
    ]
    return render(request, 'queue_app/service_list.html', {'services': services})

def analytics(request):
    context = {
        'total_tokens': 142,
        'completed': 128,
        'waiting': 8,
        'cancelled': 6,
        'days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'daily_data': [120, 135, 110, 142, 160, 90, 75],
        'completed_perc': 90,
        'waiting_perc': 6,
        'cancelled_perc': 4,
        'summary': {'total': 142, 'waiting': 8, 'completed': 128, 'cancelled': 6},
        'services': [
            {'name': 'Document Verification', 'count': 45},
            {'name': 'Token Issue', 'count': 38},
            {'name': 'Payment Counter', 'count': 32},
            {'name': 'Enquiry', 'count': 27},
        ]
    }
    return render(request, 'queue_app/analytics.html', context)

def notifications(request):
    notifications = [
        {'title': 'Counter 3 is now Free', 'time': '2 min ago', 'type': 'success'},
        {'title': 'Token #A105 Completed', 'time': '5 min ago', 'type': 'info'},
        {'title': 'Staff Raj marked as Inactive', 'time': '10 min ago', 'type': 'warning'},
    ]
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})
    
def settings(request):
    return render(request, 'queue_app/settings.html')

# Staff wale functions
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'queue_app/staff_list.html', {'staff_list': staff})

def staff_add(request):
    if request.method == 'POST':
        try:
            Staff.objects.create(
                full_name=request.POST.get('full_name'),
                employee_id=request.POST.get('employee_id'),
                department=request.POST.get('department'),
                service=request.POST.get('service'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),  # <-- YE MISS THA
                status=request.POST.get('status')
            )
            messages.success(request, "Staff Added Successfully")
            return redirect('staff_list')
        except Exception as e:
            messages.error(request, f"Error: {e}")

    return render(request, 'queue_app/staff_form.html')
def staff_edit(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, "Staff Updated Successfully")
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'queue_app/staff_form.html', {'form': form, 'title': 'Edit Staff'})

def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    staff.delete()
    messages.success(request, "Staff Deleted")
    return redirect('staff_list')