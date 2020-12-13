from djoser.serializers import TokenSerializer
from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'name', 'teacher', 'link', 'period']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    classes = ClassroomSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'classes']

class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user']

class ClassroomDetailSerializer(serializers.ModelSerializer):
    student = ProfileDetailSerializer()
    class Meta:
        model = Classroom
        fields = ['id', 'name', 'teacher', 'link', 'period', 'student']
