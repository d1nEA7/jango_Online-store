from itertools import product
from urllib import request

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
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

class OwnerOrModeratorMixin(UserPassesTestMixin):
    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user or self.request.user.has_perm("catalog.delete_product"
        )
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


class ProductUpdateView(LoginRequiredMixin, OwnerOrModeratorMixin, UpdateView):
    model = Product
    template_name = "catalog/category_update.html"
    context_object_name = "Product"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")



class ProductDeleteView(LoginRequiredMixin,OwnerOrModeratorMixin, DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:product_list")





class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"
#===================================================================================================================

# Create your views here.




class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "catalog.can_unpublish_product"

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_published = Product.Status.UNPUBLISHED
        product.save()
        return HttpResponseRedirect(
        reverse("catalog:product_detail", kwargs={"pk": product.pk})
        )
