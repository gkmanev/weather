# Generated by Django 4.2.11 on 2024-04-09 11:17

import datetime
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('weather_data', '0007_alter_weather_timestamp'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='weather',
            managers=[
                ('today', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='weather',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 9, 14, 17, 29, 47678)),
        ),
    ]
