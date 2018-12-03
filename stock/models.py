from django.db import models

# Create your models here.
class Stock(models.Model):
    id = models.IntegerField(primary_key=True)
    current = models.IntegerField()
    product = models.ForeignKey("products.Product",models.DO_NOTHING)

"""    class Meta:
        managed = True
        db_table = 'stock'"""
