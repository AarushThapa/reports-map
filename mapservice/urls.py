from django.urls import path
from .views import BaseMapView, IncidentDetailPage

urlpatterns = [
    path("", BaseMapView.as_view(), name="index"),
    path("incident/<int:pk>/", IncidentDetailPage.as_view(), name="incident_detail")
]