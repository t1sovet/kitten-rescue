from django.db import models

# Create your models here.

class Address(models.Model):
    city = models.CharField(max_length=20)
    street = models.TextField()
    home_number = models.IntegerField()

class Kitten(models.Model):
    name = models.CharField(max_length=20)
    image = models.TextField()
    address = models.ForeignKey(Address, default="ToleBi 59", on_delete=models.SET_DEFAULT)
