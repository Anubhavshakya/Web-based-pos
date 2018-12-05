from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Stock(models.Model):
    id = models.IntegerField(primary_key=True)
    current = models.IntegerField()
    product = models.ForeignKey("products.Product", on_delete="models.CASCADE")
    user = models.ForeignKey(User, on_delete="models.CASCADE", default=None)
    class Meta:
        db_table = 'stock'
