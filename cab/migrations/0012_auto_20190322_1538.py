# Generated by Django 2.1.3 on 2019-03-22 15:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cab', '0011_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2019, 3, 22, 15, 38, 24, 453536, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2019, 3, 22, 15, 38, 48, 286938, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
