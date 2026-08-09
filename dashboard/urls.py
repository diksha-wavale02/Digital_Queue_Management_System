from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('token/', views.token_card, name='token_card'),
    path('queue/', views.queue_status, name='queue_status'),
    path('notifications/', views.notifications, name='dashboard_notifications'),
    path('history/', views.token_history, name='token_history'),
    path("", views.dashboard, name="dashboard"),
    
]


