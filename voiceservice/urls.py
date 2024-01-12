from django.urls import path
from .views import VoicePage

urlpatterns = [
    path("voice/", VoicePage.as_view(), name="voice_page")
]