from django.db import models

# Create your models here.
from django.db import models


class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name="Название продукта")
    description_product = models.CharField(
        max_length=100, verbose_name="Описание продукта", blank=True, null=True
    )
    image_product = models.ImageField(upload_to="img_products/", blank=True, null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="Категория")
    price_product = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена продукта")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Category(models.Model):
    name_category = models.CharField(max_length=100)
    description_category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["-id"]
