from rest_framework.serializers import ModelSerializer
from .models import Users


class UsersModelSerializer(ModelSerializer):

    class Meta:
        model = Users
# указываем поля, которые будут передаваться при серилизации
        fields = '__all__'
