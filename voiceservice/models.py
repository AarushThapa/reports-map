from typing import Any
from django.db import models
from baseservice.models import BaseModel
from django.contrib.auth import get_user_model
User = get_user_model()



VOICES = (
    ("male","male"),
    ("female","female")
)


ACTION_CHOICES = (
    ("open_url","Open URL"),
    ("search","Search"),
    ("respond", "Respond"),
    ("call", "Call")
)

class VoiceSettings(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    assistant_name = models.CharField(max_length=255)
    assistant_voice = models.CharField(choices=VOICES, default="male", max_length=6)

    def __str__(self):
        return self.assistant_name


class Command(BaseModel):
    command_text = models.CharField(max_length=255)
    speaking_text = models.TextField()
    url = models.URLField(null=True, blank=True)
    action = models.CharField(max_length=255, choices=ACTION_CHOICES, default="open_url")
    response = models.TextField(null=True, blank=True)

    def __str__(self, *args: Any, **kwargs: Any) -> None:
        return self.command_text

