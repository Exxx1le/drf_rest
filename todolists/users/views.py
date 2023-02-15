from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

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


# пагинация, устанавливаем лимит для конкретного класса
# при этом в settings может быть установлен другой общий лимит для приложения!
# (т.к. настройки во view приоритетны над всеми другими настройками).
class ToDoOffsetPagination(LimitOffsetPagination):
    default_limit = 2

# задаем класс представления с пагинацией


class ToDoLimitOffsetPaginatonViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoOffsetPagination
