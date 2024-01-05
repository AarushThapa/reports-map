from typing import Any
from django.shortcuts import render

from django.views.generic import TemplateView, DetailView
from .models import Incident, IncidentStatus, IncidentType


class BaseMapView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        incident_type = self.request.GET.get("incident_type")
        incident_status = self.request.GET.get("incident_status")

        incident_list = Incident.objects.all()
        incident_status_list = IncidentStatus.objects.all()
        incident_type_list = IncidentType.objects.all()

        data["incident_type_list"] = incident_type_list
        data["incident_status_list"] = incident_status_list

        data["data"] = {}

        

        if incident_status:
            if incident_status != "all":
                incident_list = incident_list.filter(incident_status__pk=incident_status)
        if incident_type:
            if incident_type != "all":
                incident_list = incident_list.filter(incident_type__pk=incident_type)

        data["incident_list"] = incident_list
        for incident in incident_list:
            data["data"][incident.pk] = {
                "name": incident.name,
                "lat": incident.lat,
                "long": incident.long,
                "incident_type": incident.incident_type.name,
                "incident_status": incident.incident_status.name,
                "date": str(incident.incident_date.time()) + " | " + str(incident.incident_date.date()),
                "remarks": incident.remarks
            }
        return data


###
# - 4135450003143978
# - NABIL ICARD
# - 08/21 - 08/25
# - 438
###


# AIzaSyCqN9JNrIqprBHDGRoEA2muI24LrFvmBfM
# 9aec9a3a015f9e64

# (g=>{var h,a,k,p="The Google Maps JavaScript API",c="google",l="importLibrary",q="__ib__",m=document,b=window;b=b[c]||(b[c]={});var d=b.maps||(b.maps={}),r=new Set,e=new URLSearchParams,u=()=>h||(h=new Promise(async(f,n)=>{await (a=m.createElement("script"));e.set("libraries",[...r]+"");for(k in g)e.set(k.replace(/[A-Z]/g,t=>"_"+t[0].toLowerCase()),g[k]);e.set("callback",c+".maps."+q);a.src=`https://maps.${c}apis.com/maps/api/js?`+e;d[q]=f;a.onerror=()=>h=n(Error(p+" could not load."));a.nonce=m.querySelector("script[nonce]")?.nonce||"";m.head.append(a)}));d[l]?console.warn(p+" only loads once. Ignoring:",g):d[l]=(f,...n)=>r.add(f)&&u().then(()=>d[l](f,...n))})({
#       key: "AIzaSyCqN9JNrIqprBHDGRoEA2muI24LrFvmBfM",
#       v: "weekly",
#     });


class IncidentDetailPage(DetailView):
    template_name = "incident_detail.html"
    model = Incident
    