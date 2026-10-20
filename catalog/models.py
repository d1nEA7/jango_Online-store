from django.db import models

# Create your models here.
from django.db import models

# class Product(models.Model):
#     name_product = models.CharField(max_length=100, verbose_name="Название продукта")
#     discription_product = models.CharField(max_length=100, verbose_name="Описание продукта", blank=True, null=True)
#     image_product = models.ImageField(upload_to='img_products/', blank=True, null=True)
#     category = models.CharField(max_length=100)
#     #price_product =


class Category(models.Model):
    name_category = models.CharField(max_length=100)
    discription_category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["-id"]



