from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "headline",
        "publication_indicator",
        "created_at",
        "number_of_views",
    )
    list_filter = ("publication_indicator",)
    search_fields = ("headline", "content")
