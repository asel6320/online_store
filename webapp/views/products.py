from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, SearchForm
from webapp.models import Product, Category
from django.views import View


class ProductListView(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = "products"
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        form = self.form
        if form.is_valid():
            return form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(title__contains=self.search_value)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form
        if self.search_value:
            context["search"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        return context

class CreateProductView(CreateView):
    template_name = "products/create_product.html"
    form_class = ProductForm


class ProductDetailView(DetailView):
    template_name = "products/product_view.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UpdateProductView(UpdateView):
    template_name = "products/update_product.html"
    form_class = ProductForm
    model = Product


class DeleteProductView(DeleteView):
    template_name = "products/delete_product.html"
    model = Product
    success_url = reverse_lazy("products")

def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'products/category_view.html', context={"categories": categories})
    else:
        category = Category.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
        )
        return redirect("products/category_view")

class CategoryProductsView(View):
    def get(self, request, title_slug, *args, **kwargs):
        category =get_object_or_404(Category, title_slug=title_slug)
        context = {"products": category.products.all(), "category_title": category.title}
        return render(request, "products/categories_products.html", context)