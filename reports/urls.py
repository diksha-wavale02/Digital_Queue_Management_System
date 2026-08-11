from django.urls import path
from . import views

urlpatterns = [

    path('', views.reports_dashboard, name='reports_dashboard'),

    path('list/', views.report_list, name='report_list'),

    path('add/', views.add_report, name='add_report'),

    path('<int:pk>/', views.report_detail, name='report_detail'),

    path('delete/<int:pk>/', views.delete_report, name='delete_report'),

]