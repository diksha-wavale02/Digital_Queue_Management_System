# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.dashboard, name='dashboard'),
#     path('queue/', views.queue_management, name='queue_management'),
#     path('service/', views.service_management, name='service_management'),
#     path('staff/', views.staff_list, name='staff_list'),
#     path('staff/add/', views.staff_add, name='staff_add'),
#     path('staff/edit/<int:pk>/', views.staff_edit, name='staff_edit'),
#     path('staff/delete/<int:pk>/', views.staff_delete, name='staff_delete'),
#     path('settings/', views.settings, name='settings'),
#     path('analytics/', views.analytics, name='analytics'),
#     path('notifications/', views.notifications, name='notifications'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('queue-management/', views.queue_management, name='queue_management'),
    path('service-management/', views.service_management, name='service_management'),
    path('analytics/', views.analytics, name='analytics'),
    path('settings/', views.settings, name='settings'),

    # Staff URLs
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/add/', views.staff_add, name='staff_add'),
    path('staff/edit/<int:pk>/', views.staff_edit, name='staff_edit'),
    path('staff/delete/<int:pk>/', views.staff_delete, name='staff_delete'),
]