from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAdminUser, BasePermission

from .models import Users, Project, ToDo
from .serializers import UsersModelSerializer, UsersSerizalizerWithFullName, ProjectModelSerializer, ToDoModelSerializer

# создание собственного класса для прав


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class UsersModelViewSet(ModelViewSet):
    #   renderer_classes = [JSONRenderer]  #чтобы сделать представление в JSON
    #   renderer_classes = [AdminRenderer] # в виде для админа
    permission_classes = [IsAdminUser]  # доступ только для админа
 # permission_classes = [StaffOnly] # для собственных прав
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer


# версионирование
class UserListAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer

    # изменяем стандартный сериализатор
    def get_serializer_class(self):
        # для версионирования QueryParameterVersioning
        # version = self.request.query_params.get('version')
        # if version == '2.0':
        #     return UsersSerizalizerWithFullName
        # return UsersModelSerializer

        # для AcceptHeaderVersioning
        # self.request.headers

        if self.request.version == '0.2':
            return UsersSerizalizerWithFullName
        return UsersModelSerializer


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
