from django.db import models

from django.contrib.auth import get_user_model
from baseservice.models import BaseModel

User = get_user_model()


class IncidentType(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class IncidentStatus(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Incident(BaseModel):
    name = models.CharField(max_length=255)
    incident_status = models.ForeignKey(IncidentStatus, on_delete=models.SET_NULL, null=True, blank=True)
    incident_type = models.ForeignKey(IncidentType, on_delete=models.SET_NULL, null=True, blank=True)

    incident_date = models.DateTimeField(auto_now=False)

    lat = models.FloatField()
    long = models.FloatField()
    remarks = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name