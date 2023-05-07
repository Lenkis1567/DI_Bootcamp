from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField (max_length=50, blank=False)
    first_name = models.CharField (max_length=50, blank=False)
    second_name = models.CharField (max_length=50, blank=False)