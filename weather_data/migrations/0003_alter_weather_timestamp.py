# Generated by Django 4.2.11 on 2024-03-26 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_data', '0002_weather_heatindex_weather_uv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 26, 15, 13, 46, 41726)),
        ),
    ]
