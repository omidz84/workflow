from rest_framework import serializers

from work_flow.models import Requests
from user.api.serializers import UserSerializer


class RequestSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()

    class Meta:
        model = Requests
        fields = ['id', 'name', 'description', 'created_by', 'status', 'parent', 'created_at']


class RequestCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Requests
        fields = ['id', 'name', 'description', 'created_by', 'created_at']


class RequestRetrieveSerializer(serializers.ModelSerializer):
    response = serializers.SerializerMethodField()

    class Meta:
        model = Requests
        fields = ['id', 'name', 'description', 'created_by', 'status', 'parent', 'created_at', 'response']

    def get_response(self, obj):
        instance = Requests.objects.filter(parent=obj)
        parent_serializer = RequestRetrieveSerializer(instance=instance, many=True)
        return parent_serializer.data


class ResponseCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Requests
        fields = ['id', 'name', 'description', 'created_by', 'status', 'parent', 'created_at']

    def create(self, validated_data):
        response = Requests.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            created_by=validated_data['created_by'],
            status=validated_data['status'],
            parent=validated_data['parent']
        )
        if response.parent.parent is None:
            parent = response.parent
            parent.status = validated_data['status']
            parent.save()
        return validated_data
