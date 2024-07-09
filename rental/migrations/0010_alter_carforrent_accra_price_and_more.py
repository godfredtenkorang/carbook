# Generated by Django 5.0.6 on 2024-07-09 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0009_needadriver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carforrent',
            name='accra_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='carforrent',
            name='car_model',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='carforrent',
            name='color',
            field=models.CharField(default='Black', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='carforrent',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='carforrent',
            name='engine_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='carforrent',
            name='image',
            field=models.ImageField(null=True, upload_to='car_for_rent'),
        ),
        migrations.AlterField(
            model_name='carforrent',
            name='outside_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='featuredcarforrent',
            name='accra_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='featuredcarforrent',
            name='car_model',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='featuredcarforrent',
            name='color',
            field=models.CharField(default='Black', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='featuredcarforrent',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='featuredcarforrent',
            name='engine_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='featuredcarforrent',
            name='outside_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
