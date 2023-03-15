from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView

from users.views import UsersModelViewSet, UserListAPIView, ProjectModelViewSet, ToDoModelViewSet

# инициализация роутера, входная точка для подключения моделей
router = DefaultRouter()
# c SimpleRouter
# router = SimpleRouter() # пропадают входные точки, нужно вручную вбивать в браузере
router.register('users', UsersModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)

# документация через модуль drf_yask
schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # прописываем токены (импорт views из authtoken)
    path('api-token-auth/', views.obtain_auth_token),
    # добавляем GraphQL
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    # UrlPathVersioning
    re_path(r'^api/(?P<version>\d.\d)/users/$', UserListAPIView.as_view()),
    # NamespaceVersioning
    re_path(r'api/users/0.1', include('users.urls', namespace='0.1')),
    re_path(r'api/users/0.2', include('users.urls', namespace='0.2')),
    # пути для документации. Для доступа к open-api описанию нужно прописать 8000/swagger.json или /swagger.yaml
    # для визуального отображения - просто /swagger/
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    # другой вариант отображения документации через /redoc/
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
