from dataclasses import dataclass
from typing import Any


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
