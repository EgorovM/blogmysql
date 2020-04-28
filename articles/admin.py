from django.contrib import admin

from . import models

import inspect


for name, cls in inspect.getmembers(models, inspect.isclass):
    if cls.__module__ == 'articles.models':
        admin.site.register(cls)
