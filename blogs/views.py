from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    template_name = "blogs/blog_create.html"
    context_object_name = "blog"
    fields = ["headline", "content", "image_preview", "publication_indicator"]
    success_url = reverse_lazy("blogs:blog_list")


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogs/blog_detail.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.number_of_views += 1
        obj.save()
        return obj


class BlogListView(ListView):
    model = Blog
    template_name = "blogs/blog_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.filter(publication_indicator=True)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["headline", "content", "image_preview", "publication_indicator"]
    template_name = "blogs/blog_update.html"
    context_object_name = "blog"
    success_url = reverse_lazy("blogs:blog_list")


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blogs/blog_delete.html"
    success_url = reverse_lazy("blogs:blog_list")
