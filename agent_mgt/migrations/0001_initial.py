# Generated by Django 2.1.5 on 2019-02-07 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_mgt', '0002_auto_20190207_0411'),
        ('area_db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('ktp_photo', models.ImageField(blank=True, upload_to='driver/ktp_photo')),
                ('bank_name', models.CharField(max_length=30)),
                ('bank_branch_name', models.CharField(max_length=30)),
                ('bank_account_number', models.CharField(max_length=30)),
                ('bank_account_name', models.CharField(max_length=50)),
                ('is_approved', models.BooleanField(default=False)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='area_db.City')),
                ('kecamatan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='area_db.Kecamatan')),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='area_db.Province')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_mgt.UserManagement')),
            ],
            options={
                'verbose_name': 'Agent',
                'verbose_name_plural': 'Agents',
            },
        ),
    ]