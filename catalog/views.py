from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog.forms import CategoryForm, ProductForm
from catalog.models import Product, Category
#========================category====================================================================

class CategoryCreateView(CreateView):
    model = Category
    template_name = "catalog/category_create.html"
    context_object_name = "category"
    form_class = CategoryForm
    success_url = reverse_lazy("catalog:category_list")

class CategoryDetailView(DetailView):
    model = Category
    template_name = "catalog/category_detail.html"
    context_object_name = "category"

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "catalog/category_update.html"
    context_object_name = "category"
    form_class = CategoryForm
    success_url = reverse_lazy("catalog:category_list")

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "catalog/category_delete.html"
    success_url = reverse_lazy("catalog:category_list")

class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category_list.html"
    context_object_name = "categories"
#=========================================product=======================================================

class ProductCreateView(CreateView):
    model = Product
    template_name = "catalog/product_create.html"
    context_object_name = "product"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "catalog/category_update.html"
    context_object_name = "Product"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:product_list")

class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"

# Create your views here.


def contacts(request):
    return render(request, "contacts.html")

