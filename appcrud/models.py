from django.db import models
from django.forms import CharField

# Create your models here.
class ProdectDetails(models.Model):
    product_name=models.CharField(max_length=255)
    description=models.TextField()
    quantity=models.IntegerField()
    price=models.IntegerField()
