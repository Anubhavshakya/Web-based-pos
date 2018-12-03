from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.ForeignKey(User, on_delete="models.CASCADE", default=None)
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=True)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=255,null=True)
    salary = models.IntegerField(null=True)
    role = models.TextField(null=True)

    class Meta:
        managed = True
        db_table = 'employee'