import graphene
from web.datasets.models import File

from .types import FileType


class CreateFile(graphene.Mutation):
    file = graphene.Field(FileType)

    class Arguments:
        url = graphene.String(required=True)
        content_type = graphene.Int(required=True)
        object_id = graphene.Int(required=True)

    def mutate(self, info, url, content_type, object_id):
        file = File(url=url, content_type=content_type, object_id=object_id)
        return CreateFile(file=file)


class Mutation(graphene.ObjectType):
    create_file = CreateFile.Field()
