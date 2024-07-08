from django.urls import path

from webapp.views import index, create_product, product_view, category_view, update_product, delete_product, \
    CategoryProductsView

urlpatterns = [
    path('', index, name='products'),
    path('products', index, name='products'),
    path('products/add/', create_product, name='create_product'),
    path('products/<int:pk>/', product_view, name='product_view'),
    path('categories/add/', category_view, name='category_view'),
    path('products/<int:pk>/update/', update_product, name='update_product'),
    path('products/<int:pk>/delete/', delete_product, name='delete_product'),
    path('category/<slug:title_slug>/', CategoryProductsView.as_view(), name='category_products')
]