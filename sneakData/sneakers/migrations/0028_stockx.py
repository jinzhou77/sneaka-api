# Generated by Django 3.2.4 on 2021-08-30 05:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0027_delete_stockx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stockx',
            fields=[
                ('analyze_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('analyze_target_date', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('average_price', models.CharField(max_length=255, null=True)),
                ('high_price', models.CharField(max_length=255, null=True)),
                ('low_price', models.CharField(max_length=255, null=True)),
                ('number_of_trades', models.IntegerField()),
                ('publish_date', models.CharField(max_length=255)),
                ('sneaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sneakers.detail')),
            ],
        ),
    ]
