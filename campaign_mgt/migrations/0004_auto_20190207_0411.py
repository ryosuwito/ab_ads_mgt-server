# Generated by Django 2.1.5 on 2019-02-07 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign_mgt', '0003_auto_20190204_0804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='name',
            new_name='title',
        ),
    ]
