# Generated by Django 2.1.3 on 2018-12-05 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20181205_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='reorder_level',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.IntegerField(null=True),
        ),
    ]
