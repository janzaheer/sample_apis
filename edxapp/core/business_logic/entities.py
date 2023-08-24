from dataclasses import dataclass
from typing import Any

"""
LogEntry.objects.log_action(
                user_id=user_id,
                content_type_id=None,
                object_id=None,
                object_repr='Greeting',
                action_flag=2,  # Change this according to log action codes
                change_message=f'Greeting: {greeting_text}'
            )
"""


@dataclass
class LogsEntity:
    user_id: int
    object_id: int
    object_repr: str
    message: str
    content_type_id: int = None
    action_flag: int = 1

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'content_type_id': self.content_type_id,
            'object_id': self.object_id,
            'object_repr': self.object_repr,
            'action_flag': self.action_flag,
            'change_message': f'{self.object_repr}: {self.message}',

        }


@dataclass
class GreetingEntity:
    user: Any
    text: str

    def to_dict(self):
        return {
            'user': self.user,
            'text': self.text
        }
