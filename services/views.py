from django.shortcuts import render,redirect
from .models import Service


# Create your views here.
# Add Service
def add_service(request):
    if request.method == "POST":
        service_name = request.POST.get("service_name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        duration = request.POST.get("duration")

        Service.objects.create(
            service_name=service_name,
            description=description,
            price=price,
            duration=duration
        )
        return redirect("view_service")

    return render(request, "services/add_service.html")

# View Service
def view_service(request):
    data = Service.objects.all()
    return render(request, "services/view_service.html", {"data": data})


# Update Service
def update_service(request, id):
    service = Service.objects.get(id=id)

    if request.method == "POST":
        service.service_name = request.POST.get("service_name")
        service.description = request.POST.get("description")
        service.price = request.POST.get("price")
        service.duration = request.POST.get("duration")
        service.save()

        return redirect("view_service")

    return render(request, "services/update_service.html", {"service": service})


# Delete Service
def delete_service(request, id):
    service = Service.objects.get(id=id)
    service.delete()
    return redirect("view_service")

