# Generated by Django 2.1.5 on 2019-02-13 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_mgt', '0009_vehiclemodel_vehicle_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclemodel',
            name='vehicle_type',
        ),
    ]