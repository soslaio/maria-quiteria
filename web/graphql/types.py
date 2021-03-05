import graphene
from django.contrib.postgres.search import SearchVectorField
from graphene_django import DjangoObjectType
from graphene_django.converter import convert_django_field
from web.datasets.models import (
    CityCouncilAgenda,
    CityCouncilAttendanceList,
    CityCouncilBid,
    CityCouncilContract,
    CityCouncilExpense,
    CityCouncilMinute,
    CityCouncilRevenue,
    CityHallBid,
    CityHallBidEvent,
    File,
    Gazette,
    GazetteEvent,
)


@convert_django_field.register(SearchVectorField)
def convert_json_field_to_string(field, registry=None):
    return graphene.String()


class FileType(DjangoObjectType):
    class Meta:
        model = File
        fields = ("id", "url", "content")


class CityCouncilAgendaType(DjangoObjectType):
    class Meta:
        model = CityCouncilAgenda
        fields = "__all__"


class CityCouncilAttendanceListType(DjangoObjectType):
    class Meta:
        model = CityCouncilAttendanceList
        fields = "__all__"


class CityCouncilContractType(DjangoObjectType):
    class Meta:
        model = CityCouncilContract
        fields = "__all__"


class CityCouncilExpenseType(DjangoObjectType):
    class Meta:
        model = CityCouncilExpense
        fields = "__all__"


class CityCouncilMinuteType(DjangoObjectType):
    class Meta:
        model = CityCouncilMinute
        fields = "__all__"


class GazetteType(DjangoObjectType):
    files = graphene.List(FileType)

    def resolve_files(self, info, **kwargs):
        return File.objects.filter(object_id=self.id)

    class Meta:
        model = Gazette
        fields = "__all__"


class GazetteEventType(DjangoObjectType):
    class Meta:
        model = GazetteEvent
        fields = "__all__"


class CityHallBidType(DjangoObjectType):
    class Meta:
        model = CityHallBid
        fields = "__all__"


class CityHallBidEventType(DjangoObjectType):
    class Meta:
        model = CityHallBidEvent
        fields = "__all__"


class CityCouncilBidType(DjangoObjectType):
    class Meta:
        model = CityCouncilBid
        fields = "__all__"


class CityCouncilRevenueType(DjangoObjectType):
    class Meta:
        model = CityCouncilRevenue
        fields = "__all__"
