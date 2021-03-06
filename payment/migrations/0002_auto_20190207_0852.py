# Generated by Django 2.1.5 on 2019-02-07 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=50, null=True)),
                ('periode', models.IntegerField()),
                ('license_no', models.CharField(max_length=10, null=True)),
                ('vehicle_type', models.CharField(max_length=20, null=True)),
                ('campaign_name', models.CharField(max_length=50, null=True)),
                ('mileage', models.IntegerField()),
                ('verified_date', models.DateTimeField(null=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
