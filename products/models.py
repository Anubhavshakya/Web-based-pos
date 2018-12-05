from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete="models.CASCADE", default=None)

    class Meta:
        db_table = 'category'

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    barcode = models.CharField(unique=True, max_length=25, blank=True, null=True)
    unit_price = models.IntegerField(null=True)
    reorder_level = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete="models.CASCADE", default=None)
    user = models.ForeignKey(User, on_delete="models.CASCADE", default=None)

    class Meta:
        db_table = 'product'