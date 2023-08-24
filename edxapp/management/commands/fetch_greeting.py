from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = 'Fetches a greeting using OAuth2 access token'

    def handle(self, *args, **options):
        token_url = "http://127.0.0.1:8000/o/token/"
        client_id = "F2FNUrrAhYKIeHVykYnCnrrdM7BFAD7X5GBsziWt"
        client_secret = "pbkdf2_sha256$600000$dTS2V6RDrnkAVLY35ARpzr$ldJmymLKq7npuYyGZJvk3tCksUhHM62FG8GJMECRtsE="

        data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
        }

        response = requests.post(token_url, data=data)
        access_token = response.json().get('access_token')

        # 9JoJg8paJjyxlqg8nTGS4FgOQqXvc8yPU9XqhyuyV1WryFd6lWjAYwaGYbPuudOyKtRnzZlFUkI9i4TUZvOam9WxRMpnJzjuPF5PvoU4hjif7bxmn5ooIxVOqdcd6A2S

        endpoint_url = "http://127.0.0.1:8000/api/greetings/save_greeting/"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        data = {
            'greeting': 'Hello from the OAuth2 client!'
        }

        response = requests.post(endpoint_url, json=data, headers=headers)
        self.stdout.write(self.style.SUCCESS(response.json()))
