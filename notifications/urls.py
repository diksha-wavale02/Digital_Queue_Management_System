from django.urls import path
from . import views
urlpatterns = [
    path('', views.notification_list, name='notification_list'),
    path('add/', views.add_notification, name='add_notification'),
    path('update/<int:id>/', views.update_notification, name='update_notification'),
    path('delete/<int:id>/', views.delete_notification, name='delete_notification'),
]