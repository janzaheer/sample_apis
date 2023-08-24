from django.contrib import admin
from .models import Greeting

from django.contrib.admin.models import LogEntry


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    readonly_fields = ('content_type', 'user', 'action_time')


@admin.register(Greeting)
class GreetingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'text', 'created_at')
    search_fields = ('text',)
