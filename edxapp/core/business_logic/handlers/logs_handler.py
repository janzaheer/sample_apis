from dataclasses import dataclass

from django.contrib.admin.models import LogEntry

from edxapp.core.business_logic.entities import LogsEntity


@dataclass
class LogsHandler:
    user_id: int
    object_id: int
    object_repr: str
    message: str

    def get_entity(self):
        return LogsEntity(
            user_id=self.user_id,
            object_id=self.object_id,
            object_repr=self.object_repr,
            message=self.message
        )

    def persist_logs(self):
        entity = self.get_entity()
        LogEntry.objects.log_action(**entity.to_dict())