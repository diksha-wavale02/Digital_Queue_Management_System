# notifications/urls.py
from django.urls import path
from . import views

app_name = 'notification'

urlpatterns = [
    path('', views.notifications, name='notifications'),
    path('list/', views.notification_list, name='notification_list'),
    path('mark-read/<int:pk>/', views.mark_as_read, name='mark_as_read'),
    path('delete/<int:pk>/', views.delete_notification, name='delete_notification'),
    path('create/', views.create_notification, name='create_notification'),
    # path('add/', views.add_notification, name='add_notification'),  <-- YE LINE HATA DO
]