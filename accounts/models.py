from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

"""class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=50)
    email_id = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    mobile = models.CharField(unique=True, max_length=25)
    log_time = models.DateTimeField(default=datetime.now, blank=True) 
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'"""
#Create A User Profile 
"""class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='userprofile')
    address = models.CharField(max_length=255)
    mobile = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = True;
        db_table = 'userprofile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Userprofile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()"""

