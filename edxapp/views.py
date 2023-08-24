from rest_framework import mixins as rest_framework_mixins, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.contrib.admin.models import LogEntry

from edxapp.models import Greeting
from edxapp.serializers import GreetingSerializer, CreateGreetingSerializer
from openedx.mixins import LimitOwnedObjectsOnly


class GreetingViewSet(
    LimitOwnedObjectsOnly,
    rest_framework_mixins.ListModelMixin,
    rest_framework_mixins.RetrieveModelMixin,
    rest_framework_mixins.CreateModelMixin,
    rest_framework_mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Greeting.objects.all().order_by('-created_at')
    serializer_class = GreetingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = CreateGreetingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            obj = serializer.save()
            data = GreetingSerializer(instance=obj, context={'request': request}).data
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
