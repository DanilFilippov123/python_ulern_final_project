from django.db import models
from django.urls import reverse


# Create your models here.

class TableGraphicPair(models.Model):
    title = models.CharField(max_length=200)
    graphic_title = models.CharField(max_length=150)
    graphic = models.ImageField(upload_to="graphics/")
    table_title = models.CharField(max_length=150)
    table = models.FileField(upload_to="tables/")

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True, blank=True)
    graphics_and_tables = models.ManyToManyField(TableGraphicPair, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get_article', args=[self.pk])
