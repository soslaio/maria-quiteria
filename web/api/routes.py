from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from web.api.views import (
    CityCouncilAgendaView,
    CityCouncilAttendanceListView,
    GazetteView,
    HealthCheckView,
)

router = routers.DefaultRouter()
router.register("health-check", HealthCheckView, basename="health-check")
router.register("gazettes", GazetteView, basename="gazettes")

doc_view = TemplateView.as_view(
    template_name="swagger-ui.html", extra_context={"schema_url": "schema"}
)
schema_view = get_schema_view(
    title="Maria Quitéria",
    description="API com dados do município de Feira de Santana.",
    version="1.0.0",
)

urlpatterns = [
    path("", include(router.urls)),
    path("docs", doc_view, name="docs"),
    path("schema", schema_view, name="schema"),
    path(
        "city-council/agenda/",
        CityCouncilAgendaView.as_view(),
        name="city-council-agenda",
    ),
    path(
        "city-council/attendance-list/",
        CityCouncilAttendanceListView.as_view(),
        name="city-council-attendance-list",
    ),
]
