from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phonenum = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_joined = models.CharField(max_length=255)
    isAdmin = 'Admin'
    is_superuser = models.IntegerField()
    if is_superuser==0:
        isAdmin = 'Thuong'

    class Meta:
        managed = False
        db_table = 'auth_user'