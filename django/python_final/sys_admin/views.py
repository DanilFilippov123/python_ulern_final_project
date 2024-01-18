from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from .models import *


# Create your views here.

def get_article(request: HttpRequest, article_pk: int | None = None) -> HttpResponse:
    context = {
        "articles": Article.objects.all()
    }
    if article_pk is not None:
        context["current_article"] = Article.objects.get(pk=article_pk)
    else:
        try:
            context["current_article"] = Article.objects.get(title="Главная страница")
        except Article.DoesNotExist:
            raise Http404("Page Not Found")
    return render(request, 'base.html', context)
