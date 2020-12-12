from django.http import HttpResponse
from django.views.generic import View
from django.db import Error, OperationalError
from psycopg2 import errorcodes
from functools import wraps
from rest_framework import status
from .serializers import *
import time
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
def retry_on_exception(view, num_retries=3, on_failure=HttpResponse(status=500), delay_=0.5, backoff_=1.5):
    @wraps(view)
    def retry(*args, **kwargs):
        delay = delay_
        for i in range(num_retries):
            try:
                return view(*args, **kwargs)
            except OperationalError as ex:
                if i == num_retries - 1:
                    return on_failure
                elif getattr(ex.__cause__, 'pgcode', '') == errorcodes.SERIALIZATION_FAILURE:
                    time.sleep(delay)
                    delay *= backoff_
                else:
                    return on_failure
            except Error as ex:
                return on_failure
    return retry


class PingView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("python/django", status=200)


class GetProfile(APIView):
    serializer_class = ProfileSerializer
    lookup_url_kwarg = 'id'

    def get(self, request):
        pk = request.GET.get(self.lookup_url_kwarg)

        if pk:
            profile = User.objects.filter(id=pk)
            if profile.exists():
                user_profile = Profile.objects.get(user=profile[0])
                data = self.serializer_class(user_profile).data
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Profile Not Found': 'Invalid Profile id.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request': 'id parameter not found in request'}, status=status.HTTP_400_BAD_REQUEST)


class CreateUser(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        username = request.data.get('username')
        email = request.data.get('email')
        queryset1 = User.objects.filter(username=username)
        queryset2 = User.objects.filter(email=email)
        if queryset1.exists() or queryset2.exists():
            pass
        else:
            user = User(email=email, username=username, password=request.data.get('password'))
            user.save()
            profile = Profile(user=user)
            profile.save()
            return Response(self.serializer_class(user).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)