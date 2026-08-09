from django.urls import path
from . import views



urlpatterns = [
    path('', views.notification_list, name='notification_list'),
    path('add/', views.add_notification, name='add_notification'),
    # path('create/', views.create_notification, name='create_notification'),
    path('update/<int:pk>/', views.update_notification, name='update_notification'),
    path('delete/<int:pk>/', views.delete_notification, name='delete_notification'),
]