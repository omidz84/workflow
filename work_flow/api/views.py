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
    queryset = Requests.objects.filter(parent=None)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return ResponseCreateSerializer
        return RequestSerializer

