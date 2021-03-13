import graphene
from web.datasets.models import CityHallBid, Gazette

from .types import CityHallBidType, GazetteType


class Query(graphene.ObjectType):
    all_gazettes = graphene.List(GazetteType)
    all_city_hall_bids = graphene.List(CityHallBidType)
    gazettes = graphene.Field(GazetteType, id_gazette=graphene.Int())

    def resolve_all_gazettes(root, info):
        return Gazette.objects.all()

    def resolve_all_city_hall_bids(root, info):
        return CityHallBid.objects.all()

    def resolve_gazettes(self, info, id_gazette):
        return Gazette.objects.get(id=id_gazette)
