# Generated by Django 5.0.6 on 2024-07-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='CarForRent',
        ),
    ]