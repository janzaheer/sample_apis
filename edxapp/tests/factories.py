import factory

from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model
from oauth2_provider.models import get_application_model

from edxapp.models import Greeting


class ApplicationFactory(DjangoModelFactory):
    user = factory.LazyAttribute(lambda x: get_user_model().objects.first())
    client_secret = 'CLIENT_SECRET'

    class Meta:
        model = get_application_model()


class GreetingFactory(DjangoModelFactory):
    user = factory.LazyAttribute(lambda x: get_user_model().objects.first())

    class Meta:
        model = Greeting
