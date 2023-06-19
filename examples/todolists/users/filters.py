from django_filters import rest_framework as filters
from .models import ToDo


class ToDoFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

# добавляем фильтрацию по выбранным полям моделей
    class Meta:
        model = ToDo
        fields = ['task_name', 'users']
