from graphene_django import DjangoObjectType
from web.datasets.models import Gazette


class GazetteType(DjangoObjectType):
    class Meta:
        model = Gazette
        fields = "__all__"
