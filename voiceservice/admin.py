from django.contrib import admin
from voiceservice.models import Command, VoiceSettings


admin.site.register([
    VoiceSettings,
    Command
])