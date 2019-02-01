# Generated by Django 2.1.5 on 2019-01-31 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(blank=True, max_length=15)),
            ],
            options={
                'verbose_name': 'Privilege',
                'verbose_name_plural': 'Privileges',
            },
        ),
        migrations.CreateModel(
            name='UserManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=15)),
                ('privilege_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_mgt.Privilege')),
            ],
            options={
                'verbose_name': 'User Management',
                'verbose_name_plural': 'Users Management',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15)),
            ],
            options={
                'verbose_name': 'User Type',
                'verbose_name_plural': 'User Types',
            },
        ),
        migrations.AddField(
            model_name='usermanagement',
            name='type_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_mgt.UserType'),
        ),
        migrations.AddField(
            model_name='usermanagement',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]