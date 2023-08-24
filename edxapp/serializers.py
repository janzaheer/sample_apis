from rest_framework import serializers

from .core.business_logic.entities import GreetingEntity
from .core.business_logic.handlers.greeting_handler import GreetingHandler
from .models import Greeting


class GreetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Greeting
        fields = '__all__'


class CreateGreetingSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, max_length=200)

    def save(self):
        entity = GreetingEntity(
            user=self.context.get('request').user,
            text=self.validated_data.get('text')
        )
        greeting = GreetingHandler(obj=entity).persist()
        return greeting
