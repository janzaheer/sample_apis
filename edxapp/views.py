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

    @action(detail=False, methods=['post'])
    def save_greeting(self, request):
        greeting_text = request.data.get('greeting')
        if greeting_text:
            if request.user.is_authenticated:
                user_id = request.user.id
            else:
                user_id = None

            # Log the greeting
            LogEntry.objects.log_action(
                user_id=user_id,
                content_type_id=None,
                object_id=None,
                object_repr='Greeting',
                action_flag=2,  # Change this according to log action codes
                change_message=f'Greeting: {greeting_text}'
            )

            # Save the greeting to the database
            Greeting.objects.create(text=greeting_text)

            # Check if greeting is "hello" and call the original greeting endpoint
            if greeting_text.lower() == 'hello':
                # Code here to call the original greeting endpoint with "goodbye"
                pass  # Placeholder for the call

            return Response({'message': 'Greeting saved successfully'})
        else:
            return Response({'message': 'Invalid greeting'}, status=400)
