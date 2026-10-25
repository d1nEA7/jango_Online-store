from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "home.html", context)


def contacts(request):
    return render(request, "contacts.html")


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        "product": product
    }

    return render(request, "product_details.html", context)