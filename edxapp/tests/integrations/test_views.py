import pytest

from edxapp.tests.factories import GreetingFactory


@pytest.mark.django_db
class TestGreetingView:
    def test_list_api_returns_http200(self, logged_user, auth_client):
        user = logged_user()

        endpoint = '/api/v1/greetings/'
        resp = auth_client(user).get(endpoint)

        assert resp.status_code == 200
        assert resp.json()['count'] == 0

    def test_list_api_with_data_returns_http200(self, logged_user, auth_client):
        user = logged_user()
        GreetingFactory.create_batch(4, text='greeting text tesitng')

        endpoint = '/api/v1/greetings/'
        resp = auth_client(user).get(endpoint)

        assert resp.status_code == 200
        assert resp.json()['count'] == 4

    def test_create_api_with_wrong_data_returns_http400(self, logged_user, auth_client):
        user = logged_user()

        endpoint = '/api/v1/greetings/'
        payload = {'message': 'here is the message'}  # Note: api requires text
        resp = auth_client(user).post(endpoint, payload)

        assert resp.status_code == 400
        assert resp.json() == {'text': ['This field is required.']}

    def test_create_api_with_correct_data_returns_http400(self, logged_user, auth_client):
        user = logged_user()

        endpoint = '/api/v1/greetings/'
        payload = {'text': 'here is the message'}  # Note: api requires text
        resp = auth_client(user).post(endpoint, payload)

        assert resp.status_code == 201
        assert resp.json()['user'] == user.id
        assert resp.json()['text'] == payload.get('text')
