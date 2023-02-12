from rest_framework.viewsets import ModelViewSet

from .models import Users, Project, ToDo
from .serializers import UsersModelSerializer, ProjectModelSerializer, ToDoModelSerializer


class UsersModelViewSet(ModelViewSet):
    #   renderer_classes = [JSONRenderer]  #чтобы сделать представление в JSON
    #   renderer_classes = [AdminRenderer] # в виде для админа
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
