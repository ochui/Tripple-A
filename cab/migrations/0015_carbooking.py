# Generated by Django 2.1.3 on 2019-04-09 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cab', '0014_company_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'Expired')], default='1', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cab.Car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Car Booking',
                'verbose_name_plural': 'Car Booking',
            },
        ),
    ]
