# Generated by Django 2.1.5 on 2019-02-04 03:20

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_mgt', '0004_auto_20190204_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpsdata',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]