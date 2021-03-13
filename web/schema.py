from graphene import Schema
from web import graphql

schema = Schema(query=graphql.Query, mutation=graphql.Mutation)
