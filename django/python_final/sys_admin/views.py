import datetime
import json

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from .models import *
import requests
from utils.hh_json_prepare import hh_json_prepare


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
    return render(request, 'article.html', context)


def get_last_jobs(request: HttpRequest) -> HttpResponse:
    context = {
        "articles": Article.objects.all()
    }

    params = {
        'text': 'NAME:Системный администратор',
        'page': 1,
        'per_page': 10,
        'date_from': (datetime.datetime.now() - datetime.timedelta(days=1)).isoformat()
    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    json_objs: list[dict] = json.loads(req.content.decode())["items"]
    req.close()

    jobs = [hh_json_prepare(json_obj) for json_obj in json_objs]
    jobs.sort(key=lambda job: job["published_at"])

    context["jobs"] = jobs

    return render(request, 'last_jobs.html', context)
