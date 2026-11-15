from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


# Create your views here.


def contacts(request):
    return render(request, "contacts.html")


# def product_details(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     context = {

#         "product": product
#     }
#
#     return render(request, "product_details.html", context)
