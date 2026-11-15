from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("list/", ProductListView.as_view(), name="products_list"),
    path("contacts/", contacts, name="contacts"),
    path(
        "product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"
    ),
]
