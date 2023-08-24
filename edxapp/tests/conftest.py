import pytest

from django.contrib.auth import get_user_model
from oauth2_provider.models import get_application_model

from edxapp.tests.factories import ApplicationFactory


@pytest.fixture
def auth_client(client, mocker):
    def _(user=None):
        mocker.patch(
            'rest_framework.permissions.IsAuthenticated.has_permission',
            return_value=True
        )
        if user:
            mocker.patch('django.contrib.auth.middleware.get_user', return_value=user)
        return client

    return _


@pytest.fixture
def logged_user(mocker):
    def _new_user(username: str = 'test_user') -> dict:
        user = get_user_model().objects.create_user(username=username, password='password')

        Application = get_application_model()
        ApplicationFactory.create(
            user=user,
            name="test-application",
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_PASSWORD,
        )

        user.refresh_from_db()
        return user

    return _new_user