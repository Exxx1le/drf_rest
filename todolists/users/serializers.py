from rest_framework.serializers import ModelSerializer
from .models import Users, Project, ToDo


class UsersModelSerializer(ModelSerializer):

    class Meta:
        model = Users
# указываем поля, которые будут передаваться при серилизации
        fields = '__all__'
        # exclude = ()
        # fields = ('first_name', 'last_name')


class ProjectModelSerializer(ModelSerializer):
    # author = UsersModelSerializer()
    class Meta:
        model = Project
        fields = '__all__'


# альтернативный вариант - передает ссылки на конкретные объекты
# class ProjectModelSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = Project
#         fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    #   authors = serializers.StringRelatedField
    class Meta:
        model = ToDo
        fields = '__all__'
