# Generated by Django 2.1.3 on 2018-12-06 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20181205_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='id',
        ),
        migrations.AddField(
            model_name='stock',
            name='stock_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
