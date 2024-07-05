# Generated by Django 5.0.6 on 2024-07-05 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_featuredcarforrent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carforrent',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='rental.category'),
        ),
        migrations.AlterField(
            model_name='featuredcarforrent',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homevehicle', to='rental.category'),
        ),
    ]
