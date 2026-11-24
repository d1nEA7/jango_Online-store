from itertools import product
from urllib import request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from catalog.forms import CategoryForm, ProductForm
from catalog.models import Product, Category

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

# ========================category====================================================================


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "catalog/category_create.html"
    context_object_name = "category"
    form_class = CategoryForm
    success_url = reverse_lazy("catalog:category_list")


class CategoryDetailView(DetailView):
    model = Category
    template_name = "catalog/category_detail.html"
    context_object_name = "category"


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "catalog/category_update.html"
    context_object_name = "category"
    form_class = CategoryForm
    success_url = reverse_lazy("catalog:category_list")


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "catalog/category_delete.html"
    success_url = reverse_lazy("catalog:category_list")


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category_list.html"
    context_object_name = "categories"


# =========================================product=======================================================


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "catalog/product_create.html"
    context_object_name = "product"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "catalog/category_update.html"
    context_object_name = "Product"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if product.owner != self.request.user:
            return HttpResponseForbidden("У вас нет прав для обновления продукта.")


        return redirect('catalog:update_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if product.owner == self.request.user or self.request.user.has_perm("catalog.delete_product"):
            product.delete()
            return redirect('catalog:product_list')
        return HttpResponseForbidden("У вас нет прав для удаления продукта.")



class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"


# Create your views here.


def contacts(request):
    return render(request, "contacts.html")
