from django.urls import path
from .views import BaseMapView

urlpatterns = [
    path("", BaseMapView.as_view(), name="index")
]