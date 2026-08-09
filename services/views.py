from django.shortcuts import render, redirect, get_object_or_404

from .models import Service

from .forms import ServiceForm


def service_list(request):

    services = Service.objects.all()

    return render(request,
                  "services/service_list.html",
                  {"services": services})


def add_service(request):

    if request.method == "POST":

        form = ServiceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("service_list")

    else:

        form = ServiceForm()

    return render(request,
                  "services/add_service.html",
                  {"form": form})


def edit_service(request, id):

    service = get_object_or_404(Service, id=id)

    if request.method == "POST":

        form = ServiceForm(request.POST,
                           instance=service)

        if form.is_valid():
            form.save()
            return redirect("service_list")

    else:

        form = ServiceForm(instance=service)

    return render(request,
                  "services/edit_service.html",
                  {"form": form})

def delete_service(request,id):

    service = get_object_or_404(Service,id=id)

    if request.method=="POST":

        service.delete()

        return redirect("service_list")

    return render(request,
                  "services/delete_service.html",
                  {"service":service})