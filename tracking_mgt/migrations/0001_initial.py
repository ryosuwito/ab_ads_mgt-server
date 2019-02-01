# Generated by Django 2.1.5 on 2019-01-31 07:37

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GpsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_no', models.CharField(db_index=True, max_length=15)),
                ('timestamp', models.DateTimeField(auto_now=True, db_index=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
