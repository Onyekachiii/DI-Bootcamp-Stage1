from django.db import models

# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=30)
    date_joined = models.DateField()
