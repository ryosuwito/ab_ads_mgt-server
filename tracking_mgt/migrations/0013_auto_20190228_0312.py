# Generated by Django 2.1.5 on 2019-02-28 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_mgt', '0012_auto_20190228_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpsdailyreport',
            name='campaign_name',
            field=models.CharField(db_index=True, default='phd', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='gpsdata',
            name='campaign_name',
            field=models.CharField(db_index=True, default='phd', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='impressiongpsdata',
            name='campaign_name',
            field=models.CharField(db_index=True, default='phd', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lastlocation',
            name='campaign_name',
            field=models.CharField(db_index=True, default='phd', max_length=255, null=True),
        ),
    ]
