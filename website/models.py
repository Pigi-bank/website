from django.db import models

# Create your models here.
class Subscribers(models.Model):
  name = models.CharField(max_length=50)
  phone_number=models.IntegerField(default=0)
  email = models.EmailField()