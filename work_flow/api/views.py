from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import RequestCreateSerializer, RequestSerializer, ResponseCreateSerializer, RequestRetrieveSerializer
from work_flow.models import Requests


class RequestView(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action == 'retrieve':
            return Requests.objects.all()
        return Requests.objects.filter(parent=None)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return RequestCreateSerializer
        elif self.action == 'retrieve':
            return RequestRetrieveSerializer
        return RequestSerializer


class ResponseView(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        group_supervisor = Group.objects.get(name='سرپرست')
        group_manager = Group.objects.get(name='مدیر')
        group_user = self.request.user.groups.all()
        if group_supervisor in group_user:
            return Requests.objects.filter(status='posted', parent=None)
        elif group_manager in group_user:
            return Requests.objects.filter(status='accepted_supervisor', parent=None)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return ResponseCreateSerializer
        return RequestSerializer

