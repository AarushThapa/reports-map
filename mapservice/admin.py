from django.contrib import admin
from mapservice.models import IncidentType, IncidentStatus, Incident


admin.site.register([
    Incident,
    IncidentStatus,
    IncidentType
])