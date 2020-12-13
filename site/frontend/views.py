from django.shortcuts import render


# Create your views here.
def login_view(request):
    return render(request, 'frontend/login.html')


def logout_view(request):
    pass


def register_view(request):
    return render(request, 'frontend/register.html')


def home_view(request):
    pass