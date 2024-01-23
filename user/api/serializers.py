from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'groups', 'is_staff', 'is_superuser']

