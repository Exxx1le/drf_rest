from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Project(models.Model):
    name = models.CharField(max_length=64)
    author = models.OneToOneField(Users, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class ToDo(models.Model):
    task_name = models.CharField(max_length=128)
    text = models.TextField(null=True, blank=True)
    users = models.ManyToManyField(Users)

    def __str__(self) -> str:
        return self.task_name
