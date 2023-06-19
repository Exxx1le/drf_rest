from django.urls import re_path
from .views import UserListAPIView


# обязательно для NamespaceVersioning
# app_name = "users"

# urlspatterns = [
# добавление пути для версий api для URLPathVersioning
# re_path(r'^api/(?P<version>\d.\d)/users/$', UserListAPIView.as_view())
# добавление пути версии для NamespaceVersioning
# re_path(r"", UserListAPIView.as_view())
# ]
