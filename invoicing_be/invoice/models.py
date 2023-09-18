from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class Invoice(models.Model):
    invoice_id = models.IntegerField()
    client_name = models.CharField(max_length=200)
    date = models.DateField()

class Item(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items")
    desc = models.TextField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    
    
class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200, validators=[MinLengthValidator(6)])