from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from api.models import *

from .forms import *


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            prof = Profile(user=user)
            prof.save()

            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "frontend/register.html", {"form": form})


@login_required
def home_view(request):
    return render(
        request,
        "frontend/temp.html",
        {
            "classes": Classroom.objects.filter(
                student=Profile.objects.get(user=request.user)
            )
        },
    )


@login_required
def class_form_view(request):
    if request.method == "POST":
        form = ClassroomForm(request.POST)
        if form.is_valid():
            class_i = Classroom(
                student=Profile.objects.get(user=request.user),
                name=form.cleaned_data.get("name"),
                teacher=form.cleaned_data.get("teacher"),
                link=form.cleaned_data.get("link"),
                period=form.cleaned_data.get("period"),
            )
            class_i.save()
            return redirect("home")

    else:
        form = ClassroomForm

    return render(request, "frontend/classroomForm.html", {"form": form})


@login_required
def classroom_view(request, id):
    classroom = Classroom.objects.get(id=id)
    if classroom.student.user.pk != request.user.pk:
        return HttpResponseForbidden('You do not have access to this class')
    return render(request, "frontend/class.html", {'class': classroom})


def classroom_edit_view(request, id):
    classroom = Classroom.objects.get(id=id)
    if classroom.student.user.pk != request.user.pk:
        return HttpResponseForbidden('You do not have access to this class')


    if request.method == 'POST':
        form = ClassroomForm(request.POST, instance=classroom)

        if form.is_valid():
            classroom = form.save()
            classroom.save()
            return redirect(f'out/classes/{id}')

    form = ClassroomForm(instance=classroom)

    return render(request, 'frontend/editClassroom.html', {'form': form})