# Generated by Django 2.1.5 on 2019-02-08 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgt', '0008_auto_20190208_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermanagement',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
