from django.db import models

# Create your models here.

from django.db import models


class Blog(models.Model):
    headline = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое", blank=True, null=True)
    image_preview = models.ImageField(
        upload_to="img_preview/", blank=True, null=True, verbose_name="изображение"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    publication_indicator = models.BooleanField(
        default=True, verbose_name="Признак публикации"
    )
    number_of_views = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = "Заголовок"
        verbose_name_plural = "Заголовки"
