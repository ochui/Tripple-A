# Generated by Django 2.1.3 on 2019-03-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab', '0012_auto_20190322_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
            preserve_default=False,
        ),
    ]