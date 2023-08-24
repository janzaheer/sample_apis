class TestGreetingView:
    def test_greeting_list_api_with_wrong_endpoint_returns_http404(self, client):
        endpoint = '/api/v1/greetingwrong/'
        resp = client.get(endpoint)

        assert resp.status_code == 404

    def test_greeting_create_api_with_no_authentication_returns_401(self, client):
        payload = {'text': 'Text'}
        endpoint = '/api/v1/greetings/'
        resp = client.get(endpoint, payload)

        assert resp.status_code == 401
