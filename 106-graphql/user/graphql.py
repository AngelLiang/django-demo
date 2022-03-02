from graphene_django import DjangoObjectType
import graphene

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ('password',)
        filter_fields = ('username',)

class GroupType(DjangoObjectType):
    class Meta:
        model = Group


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user_by_username = graphene.Field(UserType, username=graphene.String(required=True))
    groups = graphene.List(GroupType)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_user_by_username(root, info, username):
        return User.objects.filter(username=username).first()

    def resolve_groups(self, info):
        return Group.objects.all()


schema = graphene.Schema(query=Query)
