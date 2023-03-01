from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken import views
from users.views import UsersModelViewSet, ProjectModelViewSet, ToDoModelViewSet

# инициализация роутера, входная точка для подключения моделей
router = DefaultRouter()
# c SimpleRouter
# router = SimpleRouter() # пропадают входные точки, нужно вручную вбивать в браузере
router.register('users', UsersModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # прописываем токены (импорт views из authtoken)
    path('api-token-auth/', views.obtain_auth_token),
]
