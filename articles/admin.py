import inspect
from django.contrib import admin

from . import models

for m in inspect.getmembers(models, inspect.isclass):
    if m[1].__module__ == 'articles.models':
        admin.site.register(m[1])
