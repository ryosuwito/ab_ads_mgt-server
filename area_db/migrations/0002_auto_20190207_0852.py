# Generated by Django 2.1.5 on 2019-02-07 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='kecamatan',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='kelurahan',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='province',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
