from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer, GroupSerializer


class GroupView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserView(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

