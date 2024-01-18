from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = ([
                   path("", views.get_article, name="main_page"),
                   path("<int:article_pk>", views.get_article, name="get_article"),
                   path("last_jobs", views.get_last_jobs, name="last_jobs")
               ]
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
