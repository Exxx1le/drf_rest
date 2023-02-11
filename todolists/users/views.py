from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from .models import Users
from .serializers import UsersModelSerializer


class UsersModelViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer
