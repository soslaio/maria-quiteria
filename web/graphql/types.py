import graphene
from django.contrib.postgres.search import SearchVectorField
from graphene_django import DjangoObjectType
from graphene_django.converter import convert_django_field
from web.datasets.models import File, Gazette, GazetteEvent


@convert_django_field.register(SearchVectorField)
def convert_json_field_to_string(field, registry=None):
    return graphene.String()


class FileType(DjangoObjectType):
    class Meta:
        model = File
        fields = ("id", "url", "content")


class GazetteEventType(DjangoObjectType):
    class Meta:
        model = GazetteEvent
        fields = "__all__"


class GazetteType(DjangoObjectType):
    files = graphene.List(FileType)

    def resolve_files(self, info, **kwargs):
        return File.objects.filter(object_id=self.id)

    class Meta:
        model = Gazette
        fields = "__all__"
