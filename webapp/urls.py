from django.urls import path

from webapp.views import index, create_product, product_detail

urlpatterns = [
    path('', index, name='products'),
    path('create/', create_product, name='create_product'),
    path('products/<int:pk>/', product_detail, name='product_detail')
]