# Generated by Django 3.2.17 on 2023-02-12 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=128)),
                ('text', models.TextField(blank=True, null=True)),
                ('users', models.ManyToManyField(to='users.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]
