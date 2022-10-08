import email
from django.db import models

# Create your models here.

class Users(models.Model):
    firstname = models.CharField(max_length = 100, blank=True)
    middlename = models.CharField(max_length = 100, blank=True)
    lastname = models.CharField(max_length = 100, blank=True)
    username = models.CharField(max_length = 100, blank=True)
    email = models.CharField(max_length = 100, blank=True)
    password = models.CharField(max_length = 100, blank=True)
    def __str__(self):
        return self.username