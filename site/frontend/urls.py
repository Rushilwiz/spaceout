"""HackTJ2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

urlpatterns = [
    path("", home_view, name="home"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="frontend/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="frontend/logout.html"),
        name="logout",
    ),
    path("register/", register_view, name="register"),
    path("create_user/", register_view, name="create_user"),
    path("home/", home_view, name="home"),
    path("classes", class_form_view, name="classroom_form"),
    path("classes/<int:id>", classroom_view, name="class"),
    path("classes/<int:id>/edit", classroom_edit_view, name="edit_class"),
]
