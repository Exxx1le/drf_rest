import math

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from users.views import UsersModelViewSet
from users.models import Users, Project


class TestUsersViewSet(TestCase):

    # метод для инициализации данных (стартовые данные)
    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_1234'
        self.email = 'admin@mail.ru'

        self.data = {'first_name': 'Ivan', 'last_name': 'Ivanov'}
        self.data_put = {'first_name': 'Petr', 'last_name': 'Ivanov'}
        self.url = 'api/users/'
        self.admin = User.objects.create_superuser(
            username=self.name, password=self.password, email=self.email)

    # проверка на тестовый запрос
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = UsersModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # проверка авторизации
    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        view = UsersModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        force_authenticate(request, self.admin)
        view = UsersModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        client = APIClient()
        user = Users.objects.create(**self.data)
        response = client.get(f'{self.url}{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest_api(self):
        client = APIClient()
        user = Users.objects.create(**self.data)
        response = client.get(f'{self.url}{user.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin_api(self):
        client = APIClient()
        user = Users.objects.create(**self.data)
        client.login(username=self.name, password=self.password)
        response = client.get(f'{self.url}{user.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        auth = Users.objects.get(id=user.id)
        self.assertEqual(auth.first_name, 'Victor')
        self.assertEqual(auth.last_name, 'Victorov')
        client.logout()

    def tearDown(self) -> None:
        pass

    class TestMath(APISimpleTestCase):

        def test_sqrt(self):
            response = math.sqrt(4)
            self.assertEqual(response, 2)

    class TestProjectViewSet(APITestCase):

        def setUp(self) -> None:
            self.name = 'admin'
            self.password = 'admin_1234'
            self.email = 'admin@mail.ru'
            self.data_author = {'first_name': 'Ivan', 'last_name': 'Ivanov'}
            self.author = Users.objects.create(**self.data_author)
            self.data = {'name': 'Test_create', 'author': self.author}
            self.data_put = {'name': 'Test_update', 'author': self.author}
            self.url = 'api/projects/'
            self.admin = Users.objects.create_superuser(
                username=self.name, password=self.password, email=self.email)

        def test_get_list(self):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_put_admin(self):
            project = Project.objects.create(**self.data)
            self.client.login(username=self.name, password=self.password)
            response = self.client.put(
                f'{self.url}{project.id}/', {'name': 'Test_update', 'author': project.author_id})
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            project_ = Project.objects.get(id=project.id)
            self.assertEqual(project_.name, 'Test_update')
            self.client.logout()

        # рандомная герерация данных модели через миксер
        def test_put_mixer(self):
            project = mixer.blend(Project)
            self.client.login(username=self.name, password=self.password)
            response = self.client.put(
                f'{self.url}{project.id}/', {'name': 'Test_update', 'author': project.author_id})
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            project_ = Project.objects.get(id=project.id)
            self.assertEqual(project_.name, 'Test_update')
            self.client.logout()

        def test_put_mixer_field(self):
            # то же, что и в методе выше, но с добавлением названия и проверки названия проекта
            project = mixer.blend(Project, name='New_project')
            self.assertEqual(project.name, 'New_project')
            self.client.login(username=self.name, password=self.password)
            response = self.client.put(
                f'{self.url}{project.id}/', {'name': 'Test_update', 'author': project.author_id})
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            project_ = Project.objects.get(id=project.id)
            self.assertEqual(project_.name, 'Test_update')
            self.client.logout()

        def tearDown(self) -> None:
            pass
