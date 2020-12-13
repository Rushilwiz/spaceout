import time
from functools import wraps

from django.db import Error, OperationalError
from django.http import HttpResponse
from django.views.generic import View
from psycopg2 import errorcodes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import *


# Create your views here.
def retry_on_exception(
    view, num_retries=3, on_failure=HttpResponse(status=500), delay_=0.5, backoff_=1.5
):
    @wraps(view)
    def retry(*args, **kwargs):
        delay = delay_
        for i in range(num_retries):
            try:
                return view(*args, **kwargs)
            except OperationalError as ex:
                if i == num_retries - 1:
                    return on_failure
                elif (
                    getattr(ex.__cause__, "pgcode", "")
                    == errorcodes.SERIALIZATION_FAILURE
                ):
                    time.sleep(delay)
                    delay *= backoff_
                else:
                    return on_failure
            except Error as ex:
                return on_failure

    return retry


class PingView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("pong!", status=200)


class UserView(APIView):
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class ProfileView(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class ClassroomView(APIView):
    def get(self, request, format=None):
        classes = Profile.objects.get(user=request.user).classes
        serializer = ClassroomSerializer(classes, many=True)
        return Response(serializer.data)


class ClassroomDetail(APIView):
    def get(self, request, *args, **kwargs):
        class_id = self.kwargs.get("class_id", None)
        classroom = Classroom.objects.get(id=class_id)
        if request.user == classroom.student.user:
            serializer = ClassroomDetailSerializer(classroom)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
