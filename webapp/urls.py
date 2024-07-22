from django.urls import path
from django.views.generic import RedirectView

from webapp.views import ProductListView, ProductDetailView, CreateProductView, UpdateProductView, DeleteProductView
from webapp.views.products import category_view, CategoryProductsView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('', RedirectView.as_view(pattern_name='products')),
    path('create/', CreateProductView.as_view(), name='create_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('product/<int:pk>/update/', UpdateProductView.as_view(), name='update_product'),
    path('product/<int:pk>/delete/', DeleteProductView.as_view(), name='delete_product'),
    path('categories/add/', category_view, name='category_view'),
    path('category/<slug:title_slug>/', CategoryProductsView.as_view(), name='category_products')
]