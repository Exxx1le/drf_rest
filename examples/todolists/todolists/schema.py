# файл для GraphQL
import graphene
from graphene_django import DjangoObjectType

from users.models import Project, Users


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = Users
        fields = '__all__'


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    projects_by_author = graphene.List(
        ProjectType, name=graphene.String(required=True))

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_users(self, info):
        return Users.objects.all()

    def resolve_user_by_id(self, info, id):
        try:
            return Users.objects.get(ok=id)
        except Users.DoesNotExist:
            return None

    def resolve_projects_by_author(self, info, name):
        projects = Project.objects.all()
        if name:
            projects = projects.filter(author=name)
        return projects


# мутации (изменение данных через post-запрос в graphQL)
class UserMutation(graphene.Mutation):
    class Arguments:
        last_name = graphene.String(required=True)
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, last_name, id):
        user = Users.objects.get(ok=id)
        user.last_name = last_name
        user.save()
        return UserMutation(user=user)


class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
