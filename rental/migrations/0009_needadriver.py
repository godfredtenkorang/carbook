# Generated by Django 5.0.6 on 2024-07-08 21:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0008_rename_outsite_price_featuredcarforrent_outside_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NeedADriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up_location', models.CharField(max_length=100)),
                ('drop_off_location', models.CharField(max_length=100)),
                ('pick_up_date', models.CharField(blank=True, max_length=20, null=True)),
                ('drop_off_date', models.CharField(blank=True, max_length=20, null=True)),
                ('pick_up_time', models.CharField(max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Need a driver',
                'ordering': ['-pick_up_date'],
            },
        ),
    ]
