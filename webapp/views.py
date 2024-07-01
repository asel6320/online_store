from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import Product, Category

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-created_at')
    return render(request, 'index.html', context={"articles": articles})

def create_article(request):
    if request.method == 'GET':
        sections = Section.objects.all()
        return render(request, 'create_article.html', context={"sections": sections})
    else:
        article = Article.objects.create(
            title=request.POST.get("title"),
            content = request.POST.get("content"),
            author = request.POST.get("author"),
            section_id = request.POST.get("section_id")
        ) # v ideale vot zdes' doljna iiti proverka, chto priwli nujnye dannye i potom peredavat'
        #return HttpResponseRedirect(reverse("article_detail", kwargs={"pk": article.pk}))
        return redirect("article_detail", pk=article.pk)

def article_detail(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    #try:
    #    article = Article.objects.get(id=pk)
    #except Article.DoesNotExist:
    #    raise Http404
    return render(request, 'article_detail.html', context={"article": article})