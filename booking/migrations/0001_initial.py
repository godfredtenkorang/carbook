# Generated by Django 5.0.6 on 2024-07-05 19:11

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rental', '0006_rename_outsite_price_carforrent_outside_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up_location', models.CharField(max_length=100)),
                ('drop_off_location', models.CharField(max_length=100)),
                ('car_type', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pick_up_date', models.DateField(null=True)),
                ('drop_off_date', models.DateField(null=True)),
                ('pick_up_time', models.TimeField(null=True)),
                ('date_added', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.carforrent')),
            ],
            options={
                'verbose_name_plural': 'Bookings',
                'ordering': ['-date_added'],
            },
        ),
    ]
