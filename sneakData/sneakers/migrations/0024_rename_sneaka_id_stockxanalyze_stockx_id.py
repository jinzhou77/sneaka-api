# Generated by Django 3.2.4 on 2021-08-30 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0023_auto_20210830_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockxanalyze',
            old_name='sneaka_id',
            new_name='stockx_id',
        ),
    ]
