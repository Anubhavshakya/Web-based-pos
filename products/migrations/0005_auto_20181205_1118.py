# Generated by Django 2.1.3 on 2018-12-05 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=None, on_delete='models.CASCADE', to='products.Category'),
        ),
    ]
