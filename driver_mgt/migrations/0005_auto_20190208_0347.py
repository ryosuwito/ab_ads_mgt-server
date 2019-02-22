# Generated by Django 2.1.5 on 2019-02-08 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver_mgt', '0004_driver_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='forgot_token',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]