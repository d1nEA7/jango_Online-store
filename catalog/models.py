from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name_product = models.CharField(max_length=100)
    discription_product = models.CharField(max_length=100)
    image_product = models.ImageField(upload_to='products/')
    #category = models.CharField(max_length=100)
    price_product =





