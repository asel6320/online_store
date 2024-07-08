from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from webapp.models import Product, Category
from webapp.forms import ProductForm, ProductSearchForm


# Create your views here.
def index(request):
    form = ProductSearchForm(request.GET)
    products = Product.objects.all().order_by('-created_at')

    if form.is_valid():
        title_query = form.cleaned_data['title']
        products = products.filter(title__icontains=title_query)

    return render(request, 'index.html', {'products': products, 'form': form})

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect("product_view", pk=product.pk)
    else:
        form = ProductForm()

    return render(request, "create_product.html", {"form": form})

def product_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', context={"product": product})

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

def update_product(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(instance=product)
        return render(
            request, "update_product.html",
            context={"form": form}
        )
    else:
        form = ProductForm(data=request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect("product_view", pk=product.pk)
        else:
            return render(
                request,
                "update_product.html",
                {"form": form}
            )


def delete_product(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, "delete_product.html", context={"product": product})
    else:
        product.delete()
        return redirect("products")

class CategoryProductsView(View):
    def get(self, request, title_slug, *args, **kwargs):
        category =get_object_or_404(Category, title_slug=title_slug)
        context = {"products": category.products.all(), "category_title": category.title}
        return render(request, "categories_products.html", context)
