from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import (
    contacts,
    ProductListView,
    ProductDetailView,
    CategoryCreateView,
    CategoryListView,
    CategoryDetailView,
    CategoryUpdateView,
    CategoryDeleteView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", contacts, name="contacts"),
    path("category/list/", CategoryListView.as_view(), name="category_list"),
    path("category/create/", CategoryCreateView.as_view(), name="create_category"),
    path(
        "category_detail/<int:pk>/",
        CategoryDetailView.as_view(),
        name="category_detail",
    ),
    path(
        "category/update/<int:pk>/",
        CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "category/delete/<int:pk>/",
        CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path("list/", ProductListView.as_view(), name="product_list"),
    path(
        "product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"
    ),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"
    ),
]
