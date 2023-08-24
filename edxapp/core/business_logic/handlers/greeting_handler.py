import requests

from dataclasses import dataclass

from edxapp.core.business_logic.entities import GreetingEntity
from edxapp.core.business_logic.handlers.logs_handler import LogsHandler
from edxapp.models import Greeting


@dataclass
class GreetingHandler:
    obj: GreetingEntity

    def handle_logs(self, greeting_id):
        LogsHandler(
            user_id=self.obj.user.id,
            object_id=greeting_id,
            object_repr='Greetings',
            message=self.obj.text
        ).persist_logs()

    def handle_edex_greetings(self):
        data = {'greeting': self.obj.text}
        resp = requests.post('http://local.tutor:8000/greetings', json=data)
        return resp.json()

    def persist(self):
        greeting = Greeting.objects.create(**self.obj.to_dict())
        self.handle_logs(greeting_id=greeting.id)
        return greeting
