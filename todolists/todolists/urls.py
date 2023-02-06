from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from users.views import UsersModelViewSet

# инициализация роутера, входная точка для подключения моделей
router = DefaultRouter
router.register('users', UsersModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
