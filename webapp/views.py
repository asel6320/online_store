from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import Product, Category

# Create your views here.
def index(request):
    products = Product.objects.order_by('-created_at')
    return render(request, 'index.html', context={"products": products})

def create_product(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'create_product.html', context={"categories": categories})
    else:
        product = Product.objects.create(
            title=request.POST.get("title"),
            price=request.POST.get("price"),
            image_url=request.POST.get("image_url"),
            description = request.POST.get("description"),
            category_id = request.POST.get("category_id"),
        )
        return redirect("product_view", pk=product.pk)

def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'category_view.html', context={"categories": categories})
    else:
        category = Category.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
        )
        return redirect("category_view")

def product_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', context={"product": product})

