from django.urls import path
from . import views

urlpatterns = [

    path("register/", views.register, name="register"),

    path("login/", views.login, name="login"),

    path("logout/", views.logout, name="logout"),

    path("list/", views.user_list, name="user_list"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("profile/", views.profile, name="profile"),

    path("feedback/", views.feedback, name="feedback"),
    
    path('token-history/', views.token_history_view, name='token_history'),
]