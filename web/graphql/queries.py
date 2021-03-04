import graphene
from web.datasets.models import Gazette

from .types import GazetteType


class Query(graphene.ObjectType):
    all_gazettes = graphene.List(GazetteType)

    def resolve_all_gazettes(root, info):
        return Gazette.objects.all()
