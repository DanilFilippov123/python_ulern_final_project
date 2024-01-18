from django.contrib import admin
from django.db.models import QuerySet
from django.core.files import File
from .models import *
import pandas as pd
import io

# Register your models here.
admin.site.register(Article)
admin.site.register(TableGraphicPair)
