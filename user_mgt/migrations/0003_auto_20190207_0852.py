# Generated by Django 2.1.5 on 2019-02-07 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgt', '0002_auto_20190207_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermanagement',
            name='type_user',
        ),
        migrations.AddField(
            model_name='privilege',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usermanagement',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]
