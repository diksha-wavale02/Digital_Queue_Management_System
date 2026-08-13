from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, ServiceCategory


# Add Service
def add_service(request):
    categories = ServiceCategory.objects.all()

    if request.method == "POST":
        category_id = request.POST.get("category")
        name = request.POST.get("name")
        duration = request.POST.get("duration")

        category = get_object_or_404(
            ServiceCategory,
            id=category_id
        )

        Service.objects.create(
            category=category,
            name=name,
            
            duration=duration
        )

        return redirect("view_service")

    return render(
        request,
        "services/add_service.html",
        {"categories": categories}
    )


# View Service
def view_service(request):
    data = Service.objects.select_related("category").all()

    return render(
        request,
        "services/view_service.html",
        {"data": data}
    )


# Update Service
def update_service(request, id):
    service = get_object_or_404(Service, id=id)
    categories = ServiceCategory.objects.all()

    if request.method == "POST":
        category_id = request.POST.get("category")

        service.category = get_object_or_404(
            ServiceCategory,
            id=category_id
        )

        service.name = request.POST.get("name")
        service.description = request.POST.get("description")
        service.duration = request.POST.get("duration")

        service.save()

        return redirect("view_service")

    return render(
        request,
        "services/update_service.html",
        {
            "service": service,
            "categories": categories
        }
    )


# Delete Service
def delete_service(request, id):
    service = get_object_or_404(Service, id=id)
    service.delete()

    return redirect("view_service")