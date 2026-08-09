"""
URL configuration for dqms project.
"""

from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [

    # ==========================
    # Splash Screen
    # ==========================
    path(
        "",
        views.splash_view,
        name="splash"
    ),

    # ==========================
    # Home Page
    # ==========================
    path(
        "home/",
        views.home_view,
        name="home"
    ),

    # ==========================
    # Admin Panel
    # ==========================
    path(
        "admin/",
        admin.site.urls
    ),

    # ==========================
    # Users Module
    # ==========================
    path(
        "users/",
        include("users.urls")
    ),

]