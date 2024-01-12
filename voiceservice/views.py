from typing import Any
from django.shortcuts import render

from django.views.generic import TemplateView, DetailView
from .models import Command, VoiceSettings


class VoicePage(TemplateView):
    template_name = "voice.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        command_list = Command.objects.all()
        command_dict = {}
        for command in command_list:
            command_dict[command.command_text] = {"text":command.speaking_text, "url":command.url, "action_type":command.action}
        data["command_keys"] = command_dict
        data["assistant_name"]  = VoiceSettings.objects.first().assistant_name
        return data