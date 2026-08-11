from django.shortcuts import render, redirect, get_object_or_404
from .models import Report


# Dashboard
def reports_dashboard(request):
    reports = Report.objects.all().order_by('-generated_date')

    total_reports = reports.count()
    total_tokens = sum(r.total_tokens for r in reports)
    completed_tokens = sum(r.completed_tokens for r in reports)
    cancelled_tokens = sum(r.cancelled_tokens for r in reports)

    context = {
        'reports': reports,
        'total_reports': total_reports,
        'total_tokens': total_tokens,
        'completed_tokens': completed_tokens,
        'cancelled_tokens': cancelled_tokens,
    }

    return render(request, 'reports/dashboard.html', context)


# Report List
def report_list(request):
    reports = Report.objects.all().order_by('-generated_date')
    return render(request, 'reports/report_list.html', {'reports': reports})


# Add Report
def add_report(request):
    if request.method == "POST":

        Report.objects.create(
            report_name=request.POST.get("report_name"),
            report_type=request.POST.get("report_type"),
            total_tokens=request.POST.get("total_tokens"),
            completed_tokens=request.POST.get("completed_tokens"),
            cancelled_tokens=request.POST.get("cancelled_tokens"),
            average_wait_time=request.POST.get("average_wait_time"),
        )

        return redirect("report_list")

    return render(request, "reports/add_report.html")


# View Single Report
def report_detail(request, pk):
    report = get_object_or_404(Report, id=pk)
    return render(request, "reports/report_detail.html", {"report": report})


# Delete Report
def delete_report(request, pk):
    report = get_object_or_404(Report, id=pk)

    if request.method == "POST":
        report.delete()
        return redirect("report_list")

    return render(request, "reports/delete_report.html", {"report": report})