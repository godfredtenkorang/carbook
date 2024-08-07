# Generated by Django 5.0.6 on 2024-07-05 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='CarForRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('engine_type', models.CharField(max_length=100)),
                ('seater', models.IntegerField(default=5, max_length=10)),
                ('car_model', models.CharField(default='', max_length=200)),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Manuel', 'Manuel')], default='Automatic', max_length=100)),
                ('drive_type', models.CharField(choices=[('Self Drive', 'Self Drive'), ('With a Driver', 'With a Driver')], default='With a Driver', max_length=100)),
                ('color', models.CharField(default='Black', max_length=100)),
                ('image', models.ImageField(upload_to='car_for_rent')),
                ('just_accra', models.BooleanField(default=False)),
                ('outside_accra', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.category')),
            ],
            options={
                'verbose_name_plural': 'Cars For Rent',
                'ordering': ['-date_added'],
            },
        ),
    ]
